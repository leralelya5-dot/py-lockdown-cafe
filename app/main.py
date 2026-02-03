from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:

    for friend in friends:
        if "vaccine" not in friend:
            return "All friends should be vaccinated"

        if (friend["vaccine"]["expiration_date"]
                < cafe.visit_cafe.__globals__["datetime"].date.today()):
            return "All friends should be vaccinated"

    masks_to_buy = sum(
        1 for friend in friends if not friend.get("wearing_a_mask", False)
    )

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
