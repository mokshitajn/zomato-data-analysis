def load_css():
    return """
<style>

/* ---------------- Main Background ---------------- */

.stApp{
    background:#FBF1DC;
}

/* ---------------- Sidebar ---------------- */

[data-testid="stSidebar"]{
    background:#84242F;
    border-right:5px solid #F5B700;
}

[data-testid="stSidebar"] *{
    color:white;
}

/* ---------------- Hero Badge ---------------- */

.hero-badge{
    display:inline-block;
    background:#F5B700;
    color:#3B1F2B;
    padding:10px 20px;
    border-radius:30px;
    font-weight:700;
    letter-spacing:2px;
    box-shadow:4px 4px 0px #84242F;
    margin-bottom:20px;
}

/* ---------------- Titles ---------------- */

.hero-title{
    font-size:3rem;
    font-weight:800;
    color:#84242F;
    margin-bottom:5px;
}

.hero-subtitle{
    font-size:1.2rem;
    color:#5B5B5B;
    margin-bottom:30px;
}

/* ---------------- Metric Cards ---------------- */

.metric-card{
    background:white;
    padding:25px;
    border-radius:18px;
    border:2px solid #E8D4A2;
    box-shadow:6px 6px 0px #E8D4A2;
    margin-bottom:20px;
}

.metric-title{
    font-size:18px;
    color:#555;
}

.metric-value{
    font-size:42px;
    font-weight:bold;
    color:#84242F;
}

/* ---------------- Restaurant Cards ---------------- */

.restaurant-card{
    background:white;
    border-radius:20px;
    padding:22px;
    border:2px solid #E7D2A5;
    box-shadow:6px 6px 0px #E7D2A5;
    margin-bottom:20px;
    transition:0.3s;
}

.restaurant-card:hover{
    transform:translateY(-4px);
}

.restaurant-name{
    font-size:28px;
    font-weight:700;
    color:#84242F;
}

.restaurant-type{
    display:inline-block;
    background:#E6FFF7;
    color:#0B8D6C;
    padding:5px 14px;
    border-radius:20px;
    font-size:14px;
    font-weight:600;
}

.rating-badge{
    float:right;
    background:#F5B700;
    color:#3B1F2B;
    padding:6px 14px;
    border-radius:12px;
    font-weight:bold;
    box-shadow:3px 3px 0px #84242F;
}

/* ---------------- Match Score ---------------- */

.match-score{
    color:#0B8D6C;
    font-weight:bold;
    font-size:18px;
    margin-top:10px;
}

/* ---------------- Why Recommended ---------------- */

.reason{
    display:inline-block;
    background:#FFF3CD;
    color:#856404;
    padding:6px 12px;
    border-radius:15px;
    margin:4px;
    font-size:13px;
}

/* ---------------- Buttons ---------------- */

.stButton>button{

    width:100%;

    background:#84242F;

    color:white;

    font-size:20px;

    font-weight:bold;

    border-radius:15px;

    border:none;

    padding:14px;

    box-shadow:6px 6px 0px #F5B700;

    transition:.3s;

}

.stButton>button:hover{

    background:#A82F3D;

}

/* ---------------- Footer ---------------- */

.footer{

    text-align:center;

    color:#777;

    padding:30px;

    margin-top:30px;

    font-size:17px;

}

</style>
"""