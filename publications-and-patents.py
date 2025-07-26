import streamlit as st

st.title("Alina Yildir's Publications and Patents")

st.header("Patents")
patents = [
    {
        "title": "Goncharuk, V.V., Taranov, V.V., & Kurliantseva, A.Y. (2017). Device for photometric determination of nitrates in aqueous solutions. [UA Patent No. 116728]",
        "url": "https://sis.nipo.gov.ua/en/search/detail/801092/"
    },
    {
        "title": "Taranov, V.V., & Kurliantseva, A.Y. (2015). Device for determining particles. [UA Patent No. 97578]",
        "url": "https://sis.nipo.gov.ua/en/search/detail/885891/"
    }
]

for p in patents:
    st.markdown(f"- [{p['title']}]({p['url']})")

st.header("Journal Publications")
publications = [
    {
        "title": "Goncharuk, V.V., Kurliantseva, A.Y., Taranov, V.V., & Nifantova, L.S. (2016). Quality and quantitative assessment of the impact of magnetic field and ultrasound on water with different concentrations of deuterium. Journal of Water Chemistry and Technology, 38(3), 143–148.",
        "url": "https://doi.org/10.3103/S1063455X16030048"
    },
    {
        "title": "Goncharuk, V.V., Taranov, V.V., Kurliantseva, A.Y., & Syroeshkin, A.V. (2015). Phase transition in waters with different content of deuterium. Journal of Water Chemistry and Technology, 37(5), 219–223.",
        "url": "https://doi.org/10.3103/S1063455X15050021"
    },
    {
        "title": "Goncharuk, V.V., Kurliantseva, A.Y., & Taranov, V.V. (2014). Detection of heterogeneities of water medium. Journal of Water Chemistry and Technology, 36(5), 205–210.",
        "url": "https://doi.org/10.3103/S1063455X14050014"
    }
]

for pub in publications:
    st.markdown(f"- [{pub['title']}]({pub['url']})")

st.info("All publications and patents were originally published under the name Alina Kurliantseva.")
