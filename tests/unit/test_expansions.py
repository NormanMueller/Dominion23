from expansions.utils.custom_exceptions import BoardError


def test_field_return_card(base_expansion_field, card_copper):
    # GIVEN
    # WHEN
    returned_card, error = base_expansion_field.return_fieldcard("Copper")
    # THEN
    assert returned_card == card_copper
    assert error == BoardError.Empty


def test_field_return_card_board_error_nomatch(base_expansion_field):
    # GIVEN
    # WHEN
    returned_card, error = base_expansion_field.return_fieldcard("Topper")
    # THEN
    assert returned_card == None
    assert error == BoardError.NoMatch


def test_field_return_card_board_error_notavailable(base_expansion_field):
    # GIVEN
    base_expansion_field.Copper.QUANTITY = 0
    # WHEN
    returned_card, error = base_expansion_field.return_fieldcard("Copper")
    # THEN
    assert returned_card == None
    assert error == BoardError.NotAvailable
