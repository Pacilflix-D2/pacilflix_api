from core.models.tayangan import Tayangan


def merge_sort(shows: list[Tayangan]) -> list[Tayangan]:
    if len(shows) <= 1:
        return shows

    mid = len(shows) // 2
    left_half = shows[:mid]
    right_half = shows[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left: list[Tayangan], right: list[Tayangan]) -> list[Tayangan]:
    merged: list[Tayangan] = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx].get_total_views_last_week() > right[right_idx].get_total_views_last_week():
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged


def get_top_10_from_tayangan_array(shows: list[Tayangan]) -> list[Tayangan]:
    sorted_shows = merge_sort(shows=shows)
    if len(sorted_shows) >= 10:
        return sorted_shows[:10]
    else:
        return sorted_shows[:len(sorted_shows)]
