# cacti.py

def cacti_number(plot):
    if not isinstance(plot, list) or not plot:
        raise ValueError("plot must be a non-empty 2-D list")
    rows = len(plot)
    cols = None
    for r in plot:
        if not isinstance(r, list) or not r:
            raise ValueError("plot must be a non-empty 2-D list with non-empty rows")
        if cols is None:
            cols = len(r)
        if len(r) != cols:
            raise ValueError("all rows must have the same length")
        for v in r:
            if v not in (0, 1):
                raise ValueError("cells must be 0 or 1")
    
    exist = []
    for r in range(rows):
        mask = 0
        for c in range(cols):
            if plot[r][c] == 1:
                mask |= (1 << c)
        exist.append(mask)

    def no_adjacent_bits(m):
        return (m & (m << 1)) == 0

    valid_per_row = []
    all_masks = range(1 << cols)
    for r in range(rows):
        e = exist[r]
        row_valid = []
        for m in all_masks:
            if (m & e) != 0:           
                continue
            if not no_adjacent_bits(m):  
                continue
            if (m & (e << 1)) != 0:
                continue
            if (m & (e >> 1)) != 0:
                continue
            row_valid.append(m)
        valid_per_row.append(row_valid)


    dp = {0: 0}

    for r in range(rows):
        new_dp = {}
        prev_exist = exist[r - 1] if r > 0 else 0
        for prev_mask, best in dp.items():
            
            blocked_above = prev_mask | prev_exist
            for m in valid_per_row[r]:
           
                if (m & blocked_above) != 0:
                    continue
                placed = m.bit_count()
                new_best = best + placed
                if m not in new_dp or new_best > new_dp[m]:
                    new_dp[m] = new_best
        dp = new_dp

    return max(dp.values()) if dp else 0

