def pytest_addoption(parser):
    parser.addoption(
        "--skip-slow",
        action="store_true",
        default=False,
        help="Exclude tests marked as slow",
    )


def pytest_collection_modifyitems(items, config):
    """Deselect tests marked as slow if --skip-slow option is set."""

    if config.option.skip_slow is False:
        return

    selected_items = []
    deselected_items = []

    for item in items:
        if item.get_closest_marker("slow"):
            deselected_items.append(item)
        else:
            selected_items.append(item)

    config.hook.pytest_deselected(items=deselected_items)
    items[:] = selected_items
