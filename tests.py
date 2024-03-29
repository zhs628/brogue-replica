from array2d import array2d
from Architect2 import SimpleShapes, Rooms
import test_tools
import sys


if __name__ == '__main__':
    # SimpleShapes

    grid = array2d(20, 10, default=0)

    SimpleShapes.draw_rectangle(grid, 1, 5, 5, 2, 3)

    test_tools.print_grid(grid)

    grid = array2d(20, 10, default=0)

    SimpleShapes.draw_circle(grid, 1, 5, 5, 2)

    test_tools.print_grid(grid)

    # Rooms
    grid = array2d(30, 30, default=0)
    SimpleShapes.draw_circle(grid, 1, 15, 15, 4)
    size = Rooms.flood_fill(grid, 2, 1, 15, 15)
    print("fill_size =" ,size)
    print(grid)
    assert size == 61

    grid = array2d(41, 30, default=0)

    Rooms.brogue_designCircularRoom(grid)

    test_tools.print_grid(grid)

    Rooms.brogue_designCrossRoom(grid)

    test_tools.print_grid(grid)

    Rooms.brogue_designSymmetricalCrossRoom(grid)

    test_tools.print_grid(grid)

    Rooms.brogue_designChunkyRoom(grid)

    test_tools.print_grid(grid)

    Rooms.brogue_designSmallRoom(grid)

    test_tools.print_grid(grid)

    grid = array2d(20, 20, 0)
    Rooms.brogue_design_compat_cavern(grid)
    test_tools.print_grid(grid)
    
    grid = array2d(40, 40, 0)
    Rooms.brogue_design_large_east_west_cavern(grid)
    test_tools.print_grid(grid)
    
    grid = array2d(40, 40, 0)
    Rooms.brogue_design_large_north_south_cavern(grid)
    test_tools.print_grid(grid)
    
    # 生成这个房间很耗时
    # grid = array2d(100, 100, 0)  # cave房间非常大, 我们需要很大的grid来容纳它, 否则它几乎不可能在短时间内被生成
    # Rooms.brogue_design_cave(grid)
    # test_tools.print_grid(grid)
    
    # 生成随机房间
    grid = array2d(Rooms.DUNGEON_WIDTH, Rooms.DUNGEON_HEIGHT, default=0)
    doors_pos = Rooms.brogue_designRandomRoom(grid, [3,4,3,4,5,4,5,3], has_doors=True, has_hallway=True)
    for x,y in doors_pos:
        if grid.is_valid(x,y):
            grid[x,y] = 3
    test_tools.print_grid(grid)
    

    # 下面进行大规模的测试

    # check functions' accuracy in Rooms except caverns
    test_tools.test_all_rooms(
        selected_func_name=["brogue_designCircularRoom", "brogue_designCrossRoom", "brogue_designSymmetricalCrossRoom", "brogue_designChunkyRoom", "brogue_designSmallRoom"],
        test_count=100,
        selection_ratio=0.3,
        grid_width_range=(1, 50),
        grid_height_range=(1, 50),
        ignore_assertion_error=True,
        mulity_process_count=16
    )
    
    # check cavern accuracy in Rooms
    test_tools.test_all_rooms(
        selected_func_name=["cavern"],
        test_count=10,
        selection_ratio=1,
        grid_width_range=(99, 100),
        grid_height_range=(99, 100),
        ignore_assertion_error=True,
        mulity_process_count=16
    )
    
    # cave
    test_tools.test_all_rooms(
        selected_func_name=["brogue_design_cave"],
        test_count=10,
        selection_ratio=1,
        grid_width_range=(Rooms.DUNGEON_WIDTH, Rooms.DUNGEON_WIDTH),
        grid_height_range=(Rooms.DUNGEON_HEIGHT, Rooms.DUNGEON_HEIGHT),
        ignore_assertion_error=True,
        mulity_process_count=16
    )
    
    # check Rooms.brogue_designRandomRoom accuracy
    # 这里随机生成100个房间, 使用原作的grid规格
    test_tools.test_all_rooms(
        selected_func_name=["brogue_designRandomRoom"],
        test_count=100,
        selection_ratio=1,
        grid_width_range=(Rooms.DUNGEON_WIDTH, Rooms.DUNGEON_WIDTH),
        grid_height_range=(Rooms.DUNGEON_HEIGHT, Rooms.DUNGEON_HEIGHT),
        ignore_assertion_error=True,
        mulity_process_count=16,
        print_exception=True
    )

