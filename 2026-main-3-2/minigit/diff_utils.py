"""Line diff rendering for the optional Mini Git diff command."""

from __future__ import annotations


def render_line_diff(left: list[str], right: list[str]) -> list[str]:
    """Render a simple LCS-based line diff."""
    rows = len(left) + 1
    cols = len(right) + 1
    table = []
    row = 0
    while row < rows:
        table.append([0] * cols)
        row += 1
    i = len(left) - 1
    while i >= 0:
        j = len(right) - 1
        while j >= 0:
            if left[i] == right[j]:
                table[i][j] = 1 + table[i + 1][j + 1]
            elif table[i + 1][j] >= table[i][j + 1]:
                table[i][j] = table[i + 1][j]
            else:
                table[i][j] = table[i][j + 1]
            j -= 1
        i -= 1
    lines = ["Diff:"]
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] == right[j]:
            lines.append(f"  {left[i]}")
            i += 1
            j += 1
        elif table[i + 1][j] >= table[i][j + 1]:
            lines.append(f"- {left[i]}")
            i += 1
        else:
            lines.append(f"+ {right[j]}")
            j += 1
    while i < len(left):
        lines.append(f"- {left[i]}")
        i += 1
    while j < len(right):
        lines.append(f"+ {right[j]}")
        j += 1
    return lines
