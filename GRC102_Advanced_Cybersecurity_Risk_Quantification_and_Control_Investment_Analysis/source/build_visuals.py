"""Reproduce Lab 3B charts and executive PDF reporting from the stated input JSON.

This script does not edit the Excel workbook; its formulas are maintained in the XLSX.
Requires: matplotlib and reportlab.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'charts'; OUT.mkdir(exist_ok=True)
data=json.loads((ROOT/'source'/'model_inputs.json').read_text())
R=data['risks']; C=data['controls']; ASS=data['assumptions']
for r in R:
    r['sle']=r['max_loss']*ASS['realised_fraction_of_max_loss']
    r['aro']=r['probability']*ASS['max_modelled_events_per_year']
    r['ale']=r['sle']*r['aro']
for c in C:
    r=next(x for x in R if x['id']==c['risk_id'])
    c['before']=r['ale']; c['benefit']=c['before']*c['effectiveness']
    c['after']=c['before']-c['benefit']
    c['cost']=c['initial']+ASS['evaluation_years']*c['maintenance_annual']
    c['net']=c['benefit']-c['cost']; c['roi']=c['net']/c['cost']
    c['payback_months']=12*c['initial']/(c['benefit']-c['maintenance_annual']) if c['benefit']>c['maintenance_annual'] else math.inf
base=sum(r['ale'] for r in R); benefit=sum(c['benefit'] for c in C); residual=base-benefit
cost=sum(c['cost'] for c in C); net=benefit-cost; roi=net/cost
fmtmoney=lambda n: '${:,.0f}'.format(n)
fmtm=lambda n: '${:,.2f}m'.format(n/1e6)
navy='#15283F'; teal='#127A83'; gold='#C79A45'; red='#C74D58'; blue='#416B9B'; light='#EAF1F4'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':14,'axes.titleweight':'bold','axes.labelsize':10,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
def save(fig,slug):
    fig.savefig(OUT/f'{slug}.png',dpi=180,bbox_inches='tight',pad_inches=.25)
    plt.close(fig)

def barlabels(ax, rects, suffix='',mult=1,precision=2):
    for r in rects:
        v=r.get_width() if r.get_width()>r.get_height() else r.get_height()
        if r.get_width()>r.get_height():
            ax.text(r.get_width()+ax.get_xlim()[1]*.012,r.get_y()+r.get_height()/2,f'{v*mult:,.{precision}f}{suffix}',va='center',fontsize=9)
        else:
            ax.text(r.get_x()+r.get_width()/2,r.get_height()+ax.get_ylim()[1]*.02,f'{v*mult:,.{precision}f}{suffix}',ha='center',fontsize=9)

# 1: baseline ALE horizontal bar
fig,ax=plt.subplots(figsize=(9,4.3))
y=np.arange(3);vals=[r['ale']/1e6 for r in R]
bars=ax.barh(y,vals,color=[blue,red,teal],height=.53)
ax.set_yticks(y,[r['name'] for r in R]);ax.invert_yaxis();ax.set_xlim(0,max(vals)*1.18)
ax.set_xlabel('Annualised loss expectancy (USD millions)');ax.set_title('Baseline risk exposure by vulnerability')
for b,v in zip(bars,vals):ax.text(v+.3,b.get_y()+b.get_height()/2,f'${v:,.2f}m',va='center',fontsize=10)
ax.grid(axis='x',alpha=.15);save(fig,'01_ale_by_risk')
# 2: pie
fig,ax=plt.subplots(figsize=(7.4,4.6));ax.pie([r['ale'] for r in R],colors=[blue,red,teal],startangle=100,autopct='%1.1f%%',pctdistance=.74,wedgeprops={'linewidth':2,'edgecolor':'white'})
ax.legend([r['name'] for r in R],loc='center left',bbox_to_anchor=(1,0.5),frameon=False)
ax.set_title('Share of baseline annual expected loss');save(fig,'02_risk_distribution_pie')
# 3: 3x3 heat map
fig,ax=plt.subplots(figsize=(7.5,4.8))
colorgrid=[['#D1FAE5','#FDE68A','#FDE68A'],['#D1FAE5','#FDE68A','#FCA5A5'],['#FDE68A','#FCA5A5','#FCA5A5']]
# matrix rows from low to high; display top high
for iy in range(3):
    for ix in range(3):
        ax.add_patch(plt.Rectangle((ix,iy),1,1,color=colorgrid[iy][ix],ec='white',lw=4))
for r in R:
    p=r['probability'];imp=r['sle'];px=0 if imp<1e6 else 1 if imp<1e7 else 2;py=0 if p<.2 else 1 if p<.35 else 2
    ax.text(px+.5,py+.5,r['id'],ha='center',va='center',fontweight='bold',fontsize=18,color=navy)
ax.set_xlim(0,3);ax.set_ylim(0,3);ax.set_xticks([.5,1.5,2.5],['Low (<$1m)','Medium ($1m-$10m)','High (≥$10m)']);ax.set_yticks([.5,1.5,2.5],['Low (<20%)','Medium (20-<35%)','High (≥35%)']);ax.set_xlabel('Single-event loss impact (USD)');ax.set_ylabel('Assumed annual event probability');ax.set_title('Probability-impact heat map (analyst-defined bands)')
ax.tick_params(length=0);save(fig,'03_probability_impact_heatmap')
# 4: cost vs effectiveness
fig,ax=plt.subplots(figsize=(8,4.5))
for c,col in zip(C,[blue,red,teal]):
    ax.scatter(c['cost']/1000,c['effectiveness']*100,s=200,color=col,zorder=4)
    ax.annotate(c['short'],(c['cost']/1000,c['effectiveness']*100),xytext=(8,8),textcoords='offset points',fontsize=10)
ax.set_xlim(100,470);ax.set_ylim(65,102);ax.set_xlabel('First-year cost (USD thousands)');ax.set_ylabel('Claimed control effectiveness (%)');ax.set_title('Control cost versus stated effectiveness')
ax.grid(alpha=.2);save(fig,'04_cost_vs_effectiveness')
# 5 ROI horizontal
fig,ax=plt.subplots(figsize=(8.6,4.2))
rv=[c['roi']*100 for c in C];y=np.arange(3)
bars=ax.barh(y,rv,color=[blue,red,teal],height=.55)
ax.set_yticks(y,[c['short'] for c in C]);ax.invert_yaxis();ax.set_xlim(0,max(rv)*1.22)
ax.set_xlabel('First-year ROI (%)');ax.set_title('Control ROI comparison (maximum-loss base case)')
for b,v in zip(bars,rv):ax.text(v+max(rv)*.02,b.get_y()+b.get_height()/2,f'{v:,.1f}%',va='center')
ax.grid(axis='x',alpha=.2);save(fig,'05_roi_comparison')
# 6 before/after
fig,ax=plt.subplots(figsize=(8.8,4.4))
x=np.arange(3);w=.34
b1=ax.bar(x-w/2,[c['before']/1e6 for c in C],w,color=red,label='Before controls')
b2=ax.bar(x+w/2,[c['after']/1e6 for c in C],w,color=teal,label='After controls')
ax.set_xticks(x,[r['name'].replace(' authentication','\nauthentication').replace(' injection','\ninjection').replace(' hijacking','\nhijacking') for r in R]);ax.set_ylabel('Annualised expected loss (USD millions)')
ax.set_title('Risk exposure before and after mapped controls');ax.legend(frameon=False)
for bs in [b1,b2]:
    for b in bs:ax.text(b.get_x()+b.get_width()/2,b.get_height()+.3,f'${b.get_height():.2f}m',ha='center',fontsize=8)
ax.set_ylim(0,max(c['before'] for c in C)/1e6*1.18);ax.grid(axis='y',alpha=.15);save(fig,'06_before_after_risk')
# 7 stacked investment
fig,ax=plt.subplots(figsize=(8.6,4.4));x=np.arange(3)
a=np.array([c['initial']/1000 for c in C]);m=np.array([c['maintenance_annual']/1000 for c in C])
ax.bar(x,a,color=navy,label='Initial implementation');ax.bar(x,m,bottom=a,color=gold,label='Year-one maintenance')
ax.set_xticks(x,[c['short'] for c in C]);ax.set_ylabel('Cost (USD thousands)');ax.set_title('First-year control investment breakdown')
ax.legend(frameon=False);ax.set_ylim(0,470)
for i,(v,z) in enumerate(zip(a,m)):ax.text(i,v+z+7,f'${v+z:.0f}k',ha='center',fontsize=9)
ax.grid(axis='y',alpha=.15);save(fig,'07_investment_breakdown')
# 8 risk run-rate line
months=[0,1,3,6,9,12];days=[0,30,90,180,270,365]
remaining=[base-sum(c['benefit'] for c in C if c['go_live_day']<=day) for day in days]
fig,ax=plt.subplots(figsize=(9,4.4));ax.step(months,np.array(remaining)/1e6,where='post',color=teal,lw=3)
ax.scatter(months,np.array(remaining)/1e6,color=navy,s=55,zorder=5)
for mo,v in zip(months,remaining):ax.annotate(f'${v/1e6:.2f}m',(mo,v/1e6),xytext=(5,9),textcoords='offset points',fontsize=8)
ax.set_xlim(-.2,12.5);ax.set_ylim(0,39);ax.set_xticks(months)
ax.set_xlabel('Months after approval (assumed go-live dates)');ax.set_ylabel('Residual ALE run-rate (USD millions/year)');ax.set_title('Illustrative annualised risk reduction over time')
ax.grid(alpha=.2);save(fig,'08_risk_reduction_timeline')
# 9 Gantt
plan=[
('Contain API auth bypass',0,7,'30d'),('Validate exposed assets',0,14,'30d'),('Deploy WAF',0,30,'30d'),('Data access / IR readiness',0,30,'30d'),
('Deploy enhanced MFA',15,90,'90d'),('SIEM telemetry + alerting',15,90,'90d'),('WAF retest',30,45,'90d'),
('API gateway delivery',30,180,'1yr'),('MFA retest',90,105,'1yr'),('Gateway retest',180,195,'1yr'),('Quarterly risk refresh',90,365,'1yr')]
fig,ax=plt.subplots(figsize=(11,5.8));ys=np.arange(len(plan));col={'30d':teal,'90d':gold,'1yr':blue}
for i,(name,st,en,phase) in enumerate(plan):ax.barh(i,en-st,left=st,height=.66,color=col[phase])
ax.set_yticks(ys,[p[0] for p in plan]);ax.invert_yaxis();ax.set_xlim(0,380)
for day in [30,90,365]:ax.axvline(day,color=red,ls='--',lw=1,alpha=.7)
ax.set_xlabel('Days after approval (assumed schedule)');ax.set_title('Risk treatment and independent retesting plan')
ax.grid(axis='x',alpha=.15);save(fig,'09_treatment_gantt')

# ReportLab typography
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
fontbold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
if Path(font).exists():
    pdfmetrics.registerFont(TTFont('DejaVu',font));pdfmetrics.registerFont(TTFont('DejaVu-Bold',fontbold))
    BODY='DejaVu';BOLD='DejaVu-Bold'
else: BODY='Helvetica';BOLD='Helvetica-Bold'
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='T1',fontName=BOLD,fontSize=20,leading=25,textColor=colors.HexColor(navy),spaceAfter=10))
styles.add(ParagraphStyle(name='T2',fontName=BOLD,fontSize=13,leading=17,textColor=colors.HexColor(navy),spaceBefore=8,spaceAfter=6))
styles.add(ParagraphStyle(name='Txt',fontName=BODY,fontSize=9.3,leading=14,textColor=colors.HexColor('#273649'),spaceAfter=6))
styles.add(ParagraphStyle(name='Small2',fontName=BODY,fontSize=7.7,leading=11,textColor=colors.HexColor('#273649')))
styles.add(ParagraphStyle(name='KPI',fontName=BOLD,fontSize=17,leading=20,textColor=colors.HexColor(navy),alignment=TA_CENTER))
styles.add(ParagraphStyle(name='KLabel',fontName=BODY,fontSize=7.5,leading=10,textColor=colors.HexColor('#465B6E'),alignment=TA_CENTER))
styles.add(ParagraphStyle(name='TH',fontName=BOLD,fontSize=8,leading=11,textColor=colors.white))
styles.add(ParagraphStyle(name='TD',fontName=BODY,fontSize=8,leading=11,textColor=colors.HexColor('#24354A')))
P=lambda txt,style='Txt':Paragraph(str(txt),styles[style])
PAGE=landscape(A4);PW,PH=PAGE

def table(rows,widths,header=True):
    obj=Table([[P(v,'TH' if header and i==0 else 'TD') for v in row] for i,row in enumerate(rows)],colWidths=widths,repeatRows=1 if header else 0,hAlign='LEFT')
    cmds=[('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,-1),(-1,-1),.4,colors.HexColor('#DCE6EB'))]
    if header:cmds.extend([('BACKGROUND',(0,0),(-1,0),colors.HexColor(navy)),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F3F7F8')])])
    obj.setStyle(TableStyle(cmds));return obj

def pic(name,w=365,h=205):
    img=Image(str(OUT/name),width=w,height=h)
    return img

def twoimages(a,b,w=360,h=198):
    t=Table([[pic(a,w,h),pic(b,w,h)]],colWidths=[w+6,w+6],hAlign='LEFT')
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),6)]))
    return t

def footer(canvas,doc):
    canvas.setStrokeColor(colors.HexColor('#DCE6EB'));canvas.line(32,27,PW-32,27)
    canvas.setFont(BODY,7.5);canvas.setFillColor(colors.HexColor('#536879'))
    canvas.drawString(32,15,'SecureBank Financial  |  Lab 3B  |  Scenario model - not an actual loss forecast')
    canvas.drawRightString(PW-32,15,f'Adediran Eunice Adebukola  |  C11-26-CGRCE-17595  |  Page {doc.page}')

def docbuild(path,story):
    doc=SimpleDocTemplate(str(path),pagesize=PAGE,leftMargin=35,rightMargin=35,topMargin=30,bottomMargin=37,title='Lab 3B - Cybersecurity Risk Quantification',author=data['student'])
    doc.build(story,onFirstPage=footer,onLaterPages=footer)

# One-page executive dashboard: KPI + compact risk table + visuals + recommendations
kpi=[('BASELINE ALE',fmtm(base)),('RESIDUAL ALE',fmtm(residual)),('AVOIDED ALE',fmtm(benefit)),('YEAR-1 COST',fmtmoney(cost)),('YEAR-1 ROI',f'{roi*100:,.1f}%')]
cardcells=[]
for label,value in kpi:
    cardcells.append(Table([[P(value,'KPI')],[P(label,'KLabel')]],colWidths=[139],rowHeights=[30,18],style=TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor(light)),('BOX',(0,0),(-1,-1),.6,colors.HexColor('#D5E3E8')),('VALIGN',(0,0),(-1,-1),'MIDDLE')])))
cardrow=Table([cardcells],colWidths=[145]*5,hAlign='LEFT')
rs=[['Risk','Baseline ALE','After control','Financial priority']]
for r,c in zip(R,C):rs.append([r['name'],fmtmoney(r['ale']),fmtmoney(c['after']),'Critical' if r['ale']>=1e7 else 'High' if r['ale']>=1e6 else 'Moderate'])
dash=[P('EXECUTIVE DASHBOARD  |  SECUREMOBILE','T1'),P('Lead GRC analyst: Adediran Eunice Adebukola  |  Registration: C11-26-CGRCE-17595','Small2'),Spacer(1,9),cardrow,Spacer(1,12),table(rs,[285,160,160,110]),Spacer(1,12),twoimages('06_before_after_risk.png','05_roi_comparison.png',355,180),Spacer(1,10),P('<b>Recommendation:</b> Prioritise WAF deployment by day 30 and enhanced MFA by day 90; implement compensating API authentication safeguards immediately and complete gateway deployment by day 180. All dates are planning assumptions.','Small2'),P('<b>Decision caution:</b> The $35m baseline assumes the stated probabilities apply to one annual loss event and that each event incurs the supplied maximum loss. Confirm loss severity, exposure, control coverage and technical efficacy before authorising spend.','Small2')]
docbuild(ROOT/'Executive_Dashboard_One_Page.pdf',dash)

# Longer executive briefing, page breaks deliberately separated
story=[P('LAB 3B  |  ADVANCED CYBERSECURITY RISK QUANTIFICATION','T1'),P('SecureBank Financial - SecureMobile  |  Prepared by Adediran Eunice Adebukola  |  C11-26-CGRCE-17595'),P('1. Executive conclusion','T2'),P(f'The three modelled vulnerabilities produce <b>{fmtmoney(base)}</b> in illustrative annualised expected loss. The three specified controls would avoid <b>{fmtmoney(benefit)}</b> in annualised loss, leaving <b>{fmtmoney(residual)}</b> residual exposure. First-year investment is <b>{fmtmoney(cost)}</b> and modelled first-year ROI is <b>{roi*100:,.1f}%</b>. These are conditional scenario estimates, not observed losses or guaranteed savings.'),table(rs,[285,160,160,110]),Spacer(1,12),twoimages('01_ale_by_risk.png','02_risk_distribution_pie.png',355,195),P('<b>Priority:</b> Database injection dominates baseline ALE (89.3%). The largest loss estimate derives from the assumption that all 500,000 records incur the full $250 per-record cost in one incident. This requires sensitivity testing and validation.','Small2'),PageBreak(),
P('2. Risk method and probability-impact view','T1'),P('<b>Calculation:</b> SLE = maximum incident loss (or exposed units × cost per unit). Assumed ARO = supplied exploit probability × one modelled event/year. ALE = SLE × assumed ARO. This is a Bernoulli, one-event annual scenario; the brief does not provide actual annual event frequency.'),
table([['Risk','Supplied probability','Model SLE','Assumed ARO','ALE','Priority']]+[[r['name'],f"{r['probability']*100:.0f}%",fmtmoney(r['sle']),f"{r['aro']:.2f}",fmtmoney(r['ale']),'Critical' if r['ale']>=1e7 else 'High' if r['ale']>=1e6 else 'Moderate'] for r in R],[210,98,113,87,119,88]),Spacer(1,10),twoimages('03_probability_impact_heatmap.png','01_ale_by_risk.png',355,195),P('<b>Priority definitions:</b> Critical ALE ≥ $10m/year; High ALE ≥ $1m/year; Moderate below $1m/year. Heat-map probability/impact cutoffs are separately defined and are not official SecureBank risk appetite.','Small2'),PageBreak(),
P('3. Control cost-benefit and residual risk','T1'),P('Control-to-risk applicability is an analyst assumption: API gateway → API authentication bypass; WAF → database injection; MFA → session hijacking. Benefits are not double-counted across controls.'),
table([['Control','Initial','Maint./yr','Avoided ALE/yr','Residual ALE/yr','Yr1 ROI','Payback']]+[[c['short'],fmtmoney(c['initial']),fmtmoney(c['maintenance_annual']),fmtmoney(c['benefit']),fmtmoney(c['after']),f"{c['roi']*100:,.1f}%",f"{c['payback_months']:.2f} months"] for c in C],[100,95,92,120,122,89,97]),Spacer(1,8),twoimages('04_cost_vs_effectiveness.png','05_roi_comparison.png',345,165),Spacer(1,5),twoimages('07_investment_breakdown.png','06_before_after_risk.png',345,165),PageBreak(),
P('4. Implementation plan, monitoring and independent retest','T1'),P('The schedule is a planning assumption, not a deployment commitment. Day 0 means management approval. Immediate containment of the API bypass should not wait for the gateway project.'),
twoimages('08_risk_reduction_timeline.png','09_treatment_gantt.png',355,215),
table([['Time horizon','Priority actions','Accountable owner','Closure evidence'],['0-30 days','Contain API auth bypass; deploy WAF; validate injection path and data exposure','API Platform / AppSec / Data Security','Retested WAF rule, secure auth control, attack simulation'],['31-90 days','Deploy enhanced MFA, centralise SIEM telemetry and alerts','IAM / SOC / Platform','MFA bypass test, alert response metrics, independent retest'],['91-365 days','Deploy gateway, retest API auth, quarterly risk refresh','API Platform / GRC / AppSec','Independent pentest, risk recalculation, governance sign-off']],[95,273,155,192]),Spacer(1,9),P('<b>Continuous monitoring:</b> Alert on suspicious transfers, repeated authentication failures, injection attempts, session anomalies, privilege changes and data-exfiltration signals. Escalate failed controls, material residual exposure and missed remediation milestones to the CISO.','Small2'),PageBreak(),
P('5. Assumptions, sensitivity and financial justification','T1'),P('<b>One-year ROI:</b> (annual avoided ALE - [initial cost + one year maintenance]) / [initial cost + one year maintenance]. <b>Payback:</b> initial investment / (annual avoided ALE - annual maintenance), expressed in years then converted to months. Payback is a steady-state simplification and does not include delayed implementation, discounting or deployment ramp-up.'),
table([['Realised severity','Baseline ALE/yr','Avoided ALE/yr','Residual ALE/yr','Yr1 net benefit','Yr1 ROI']]+[[f'{p*100:.0f}%',fmtmoney(base*p),fmtmoney(benefit*p),fmtmoney(residual*p),fmtmoney(benefit*p-cost),f'{((benefit*p-cost)/cost)*100:,.1f}%'] for p in [.1,.25,.5,1.0]],[112,126,126,126,126,99]),Spacer(1,12),P('Assumptions and limitations','T2')]
for text in [
'Annual event frequency is not supplied. We treat each probability as a one-year chance of at most one event. Different frequencies, multiple events or correlated incidents would change ALE.',
'Maximum loss is not a mean incident severity. The 10%, 25%, 50% and 100% scenarios demonstrate dependence on loss magnitude; no empirical loss distribution was supplied.',
'API gateway coverage is not proof that an application authentication bypass is fixed. WAF protection does not replace parameterised queries. MFA does not necessarily stop stolen live sessions. Validate control effectiveness independently.',
'The model excludes customer attrition, downtime, litigation, incident response, fraud recovery, regulatory jurisdiction differences, vendor deployment constraints and the time value of money.',
'Implementation timing, risk bands, event cap, and risk-to-control mapping are analyst assumptions. No budget ceiling or historical loss dataset was provided.'
]:story.append(P('• '+text,'Txt'))
story.extend([P('Recommended management decision','T2'),P('Approve technical validation and immediate compensating controls first. Subject to confirmed exploit paths and costs, sequence WAF, MFA and API gateway remediation; assign accountable owners and require independent retesting before closing findings. Recalculate the risk model using observed loss and incident data before treating the ROI figures as investment-grade forecasts.'),P('Source: Supplied Lab 3b official brief and instructor guidance screenshot. All calculations and visualisations are derived from supplied inputs and explicitly identified modelling assumptions. No external threat-frequency or cost dataset has been introduced.','Small2')])
docbuild(ROOT/'Executive_Briefing.pdf',story)

print('SUMMARY',{'baseline':base,'benefit':benefit,'residual':residual,'cost':cost,'roi_pct':roi*100,'charts':len(list(OUT.glob('*.png')))})
