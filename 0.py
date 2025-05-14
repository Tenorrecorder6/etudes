import marimo

__generated_with = "0.13.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # Fun

    ## Pretty fun, at least

    ### Third tier

    More text

    - bullets *are* ***cool***
    """
    )
    return


if __name__ == "__main__":
    app.run()
