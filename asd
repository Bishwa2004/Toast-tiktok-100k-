## Opportunities and Risks – Python & Jupyter for Capacity Analytics

Before diving in, I want to **re-emphasize** that this is a **proof of concept** — the focus is on the potential of Python in capacity analytics, not the benefit time analysis.  
We completed that analysis earlier and used it as a baseline to guide expectations.

---

### 🔴 Key Risks:

- **Data Security & Compliance**  
  Bank of America enforces strict controls over who accesses data and how it's stored or shared. Any new tool must align with governance and compliance policies.

- **Tool Limitations**  
  Python and Jupyter are powerful, but they cannot fully replace tools like **SAS**, **Excel**, or **Tableau**, especially for more advanced or embedded workflows.

- **Change Management Resistance**  
  New tools often face resistance due to existing preferences and learning curves. Adoption may take time and require training.

---

### ✅ Key Opportunities:

- **Unified Reporting**  
  Jupyter brings **code, analysis, and documentation** into a single notebook — improving transparency, reproducibility, and audit readiness.

- **Extensive Analytical Toolkit**  
  Python supports advanced modeling, forecasting, automation, and data visualization that go beyond traditional spreadsheet tools.

- **Cost Efficiency**  
  Python is **open-source**, reducing licensing costs compared to commercial tools like SAS and Tableau.

- **Repeatable Automation**  
  Scripts can supplement Excel/SAS by automating workflows and reducing manual errors — enabling consistent, scalable analysis.

- **Model Governance Readiness**  
  As capacity analytics moves toward a more model-driven approach, Python enables us to start designing **controlled, auditable workflows** that align with risk and compliance frameworks.

---

In summary, while Python isn’t a replacement today, it represents a **strong first step** toward a future of **automated, transparent, and model-driven** capacity planning.



PRESENTATION SCRIPT:


Thank you, Stacy. Great indroduction 

Hi everyone, good afternoon. I am very excited, to walk you guys through a brief overview, of one of the key projects me & stacy worked on during our internship. 
This particular iniative was for our Transcation risk moniterting team within Merchant Services, which was presented to Eric Moore. who leads TRM, to help answer some of the operational efficiency and risk monitering questions raised by our line of business unit leaders. 

What made this project special, was the exposure. We got to meet with several business leaders to understand the questions they wanted answered, and we also got to interact qith TRM and SB Credit associates, whose performance we were analyzing. This added a layer of context and connection to data, which made the analysis more meaningful. 

The Full presentation we delivered to Eric is included in the appendix, but I’ll walk you guys through the highlights here. 

We began by looking at 2024 redeploys performance year-over-year. This was important because many of the redeployed associates came from First Mortgage and faced onboarding friction due to new workflows.
Despite that, we saw a 32.04% YoY improvement in performance, whcih is measured by average completion time of Flash Alerts, across like-for-like queues(in minutes) – which is a strong indicator of operational efficiency gains.


Next, we compared the ramp-up performance of these 2024 redeploys with the Off shore associates who joined us in 2025, To find if there were any  similarities within these 2 groups. 

The short answer was yes, the ramp-up trends were similar. However, our offshore associates showed higher overall performance during onboarding. 
Most of the performance gain happened During Month 1 and Month 2, and both populations showed stabilization at Month 4 and Month 5.

Another key question from leadership was about performance variance between Analyst 2s and Analyst 3s.
What we found that Analyst 3s were 37.8% faster than Analyst 2s when working on similar queues. However, I want to emphasize that speed does not equal quality – our focus here was understanding whether performance variance was due to associate-specific factors or inherent to the queue itself.

On the right side of this slide, you’ll see our 2025 blended performance. One key trend was the impact of offshore associates who joined in February.
There was a noticeable increase in queue completion time – from 28 minutes in January to 44 minutes in February – followed by a 20.3% improvement in performance as the offshore associates ramped up quickly and even exceeded our initial capacity expectations.

Finally, the heatmap at the bottom highlights queue-level variance across the months. We saw consistent performance, with one exception in April where secondary reviews were increased to help reduce fraud losses. This shift temporarily affected queue speed due to the focus on education and review intensity.


On this slide we tried to answer 2 addtional questions on SLA impact 

First being, Do we see a shift in disposition outcomes as applications age in the queue for longer periods of time. We noticed, after the  5days mark terminations outpace maintain rates. This is what we expected to see, but it is great to verify it with numbers. 

ANd next, we looked at out SLA performance YoY?
We see that out SLA breach % has gone down indicating increased efficiency. while still seeing some seasonality. 
Also, In june 2025 SLA targets were adjusted from 4 days to 7 days resulting a lower breach rate (Yay).


Python Project:

I am going to highlight some of the key O/Rs (oppotunities and risk) of using Jupyter notebook and python for capacity analytics. 

Before we move on, I want to re- emphasise that the main focus here is the proof of concept of potentially using Python for capacity analytics and not the benefit time analysis. 
We had done the same analysis a couple weeks ago, which gave us a baseline to see what we shouold’ve expected from the results. 

Our biggest Risks here would be 
- Data security & compliance, Bank of america has very strict controls over who and how data is accessed 
- Cannot fully replace the full functionality of other tools like SAS or excel 
- Change Management Resistence.
The biggest Use case for Juptyper notebooks is that it allows to bring code and analysis and reporting into one single documentated report. 

Large set of analytical tool

Cheaper liscencing cost compared to  SAS or Tablaue 

I beleive this would be very value adding as it would make the knowledge trandfer process much better. 
Like for handoffs, audit and long term maintainability

Supplementing Excel/SAS with repeatable and automated analytics 

This is a controlable file. Similar to QA processes to the QA workbook currently used in reporting

I stornly beleive that in the future we will be using models for capacity analytics, and this could be the first step in the right dirrection because we can build control proccess for model goverence and complainaace to reduce risk of using python. 
