def clean_robot(r_start, c_start, d_start, room_map):
    n = len(room_map)
    m = len(room_map[0])

    r, c, d = r_start, c_start, d_start

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    cleaned_count = 0

    while True:
        if room_map[r][c] == 0:
            room_map[r][c] = 2
            cleaned_count += 1

        found_in_surroundings = False
        for i in range(4):
            nr_check, nc_check = r + dr[i], c + dc[i]
            if 0 <= nr_check < n and 0 <= nc_check < m:
                if room_map[nr_check][nc_check] == 0:
                    found_in_surroundings = True
                    break
        
        if not found_in_surroundings:
            back_r, back_c = r - dr[d], c - dc[d]

            if 0 <= back_r < n and 0 <= back_c < m and room_map[back_r][back_c] != 1:
                r, c = back_r, back_c
            else:
                return cleaned_count
        else:
            d = (d + 3) % 4
            front_r, front_c = r + dr[d], c + dc[d]
            if 0 <= front_r < n and 0 <= front_c < m and room_map[front_r][front_c] == 0:
                r, c = front_r, front_c
n,m=map(int,input().split())
r,c,d=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

print(clean_robot(r,c,d,arr))