import match

def test_determine_first_server():
    # # TODO: have to mock input statements # #
    assert match.determine_first_server() in ["player", "computer"]
