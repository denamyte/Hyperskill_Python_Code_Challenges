import bisect
from typing import List


class PaintingsMatch:
    def __init__(self, frames: List[int], n: int, width: int, height: int):
        self.n = n
        self.p_sizes = [width, height]  # the sizes of a painting
        self.tiles = [1, 1]  # the current size of the frame in paintings
        min_frame_size = self.define_min_frame_size()
        self.frame_index = bisect.bisect_left(frames, min_frame_size)

    def define_min_frame_size(self) -> int:
        while self.tiles[0] * self.tiles[1] < self.n:
            self.tiles[self.which_side_to_grow()] += 1

        return max(size * tile_number for size, tile_number in zip(self.p_sizes, self.tiles))

    def which_side_to_grow(self):
        return 0 if (self.tiles[0] + 1) * self.p_sizes[0] < (self.tiles[1] + 1) * self.p_sizes[1] else 1


p_match = PaintingsMatch(frames, *(int(x) for x in input().split()))
print(p_match.frame_index)
