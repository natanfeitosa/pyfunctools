from pyfunctools.pipeline import pipeline


def test_pipeline():
    pipes = pipeline(
        lambda s: s.upper(),
        lambda s: s + ' 95',
        lambda s: s.replace(' ', '-')
    )

    assert pipes('functional python') == 'FUNCTIONAL-PYTHON-95'
