import pandas as pd
import plotly.graph_objects as go

# --- Load data ---
# Place this script in the same folder as your CSV files
df = pd.read_csv("reports/file-size-analysis/size_multipliers_sheet1.csv")

# Strip whitespace from column names just in case
df.columns = df.columns.str.strip()

# Drop rows with missing values
df = df.dropna(subset=["DOC/X Size", "A-2u Multiplier", "A-1b Multiplier"])

# --- Build figure ---
fig = go.Figure()

# PDF/A-2u scatter
fig.add_trace(go.Scatter(
    x=df["DOC/X Size"],
    y=df["A-2u Multiplier"],
    mode="markers",
    name="PDF/A-2u",
    marker=dict(
        color="rgba(50, 102, 173, 0.55)",
        size=7,
        line=dict(width=0.5, color="rgba(50, 102, 173, 0.9)")
    ),
    customdata=df[["Title", "Drive"]],
    hovertemplate=(
        "<b>%{customdata[0]}</b><br>"
        "Drive: %{customdata[1]}<br>"
        "Original size: %{x} KB<br>"
        "Multiplier: %{y:.1f}×<extra>PDF/A-2u</extra>"
    )
))

# PDF/A-1b scatter
fig.add_trace(go.Scatter(
    x=df["DOC/X Size"],
    y=df["A-1b Multiplier"],
    mode="markers",
    name="PDF/A-1b",
    marker=dict(
        color="rgba(224, 123, 57, 0.55)",
        size=7,
        line=dict(width=0.5, color="rgba(224, 123, 57, 0.9)")
    ),
    customdata=df[["Title", "Drive"]],
    hovertemplate=(
        "<b>%{customdata[0]}</b><br>"
        "Drive: %{customdata[1]}<br>"
        "Original size: %{x} KB<br>"
        "Multiplier: %{y:.1f}×<extra>PDF/A-1b</extra>"
    )
))

# --- Layout ---
fig.update_layout(
    title=dict(
        text="File Size Multiplier vs. Original File Size (n=161)",
        font=dict(size=24)
    ),
    xaxis=dict(
        title="Original File Size (KB)",
        showgrid=True,
        gridcolor="rgba(0,0,0,0.07)",
        zeroline=False
    ),
    yaxis=dict(
        title="File Size Multiplier (Converted ÷ Original)",
        ticksuffix="×",
        showgrid=True,
        gridcolor="rgba(0,0,0,0.07)",
        zeroline=False
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(t=80, b=60, l=70, r=30),
    hovermode="closest"
)

# --- Save and show ---
fig.write_html("reports/file-size-analysis/size_multipliers_plot.html")
print("Saved to size_multipliers_plot.html")
fig.show()