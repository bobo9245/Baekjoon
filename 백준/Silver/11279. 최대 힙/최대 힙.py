import sys
input=sys.stdin.readline

class Heap:
    def __init__(self,data):
        self.heap_array=list()
        self.heap_array.append(None)
        self.heap_array.append(data)
    def __init__(self):
        self.heap_array=list()
        self.heap_array.append(None)

    def move_up(self, inserted_idx):
        if inserted_idx<=1:
            return False
        parent_idx=inserted_idx//2
        if self.heap_array[inserted_idx]>self.heap_array[parent_idx]:
            return True
        else:
            return False
    def move_down(self, just_idx):
        left_child_of_just_idx=just_idx*2
        right_child_of_just_idx=just_idx*2+1
        # 자식이 둘다 없음
        if left_child_of_just_idx>=len(self.heap_array):
            return False
        # 왼쪽 자식 하나만 있음
        elif right_child_of_just_idx>=len(self.heap_array):
            if self.heap_array[just_idx]<self.heap_array[left_child_of_just_idx]:
                return True
            else:
                return False
        # 자식이 둘다 있음
        else:
            # 왼쪽자식 > 오른쪽자식인 경우
            if self.heap_array[left_child_of_just_idx]>self.heap_array[right_child_of_just_idx]:
                if self.heap_array[just_idx]<self.heap_array[left_child_of_just_idx]:
                    return True
                else:
                    return False
            # 왼쪽자식 <= 오른쪽자식인 경우
            else:
                if self.heap_array[just_idx]<self.heap_array[right_child_of_just_idx]:
                    return True
                else:
                    return False
    def insert(self,data):
        # 빈경우
        if len(self.heap_array)==0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        # 아닌경우 -> 일단 맨끝에넣어
        self.heap_array.append(data)
        inserted_idx=len(self.heap_array)-1

        # 그리고 move_up하면서 parent랑 계속 비교
        while self.move_up(inserted_idx):
            parent_idx=inserted_idx//2
            self.heap_array[inserted_idx],self.heap_array[parent_idx]=self.heap_array[parent_idx],self.heap_array[inserted_idx]
            inserted_idx=parent_idx
        return True

    def pop(self):
        if len(self.heap_array) < 2:
            return 0
    
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        just_idx = 1
    
        while True:
            left_child_idx = just_idx * 2
            right_child_idx = just_idx * 2 + 1
    
            if right_child_idx >= len(self.heap_array):
                if left_child_idx < len(self.heap_array) and self.heap_array[left_child_idx] > self.heap_array[just_idx]:
                    self.heap_array[just_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[just_idx]
                    just_idx = left_child_idx
                else:
                    break
            else:
                if self.heap_array[left_child_idx] > self.heap_array[right_child_idx]:
                    if self.heap_array[just_idx] < self.heap_array[left_child_idx]:
                        self.heap_array[just_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[just_idx]
                        just_idx = left_child_idx
                    else:
                        break
                else:
                    if self.heap_array[just_idx] < self.heap_array[right_child_idx]:
                        self.heap_array[just_idx], self.heap_array[right_child_idx] = self.heap_array[right_child_idx], self.heap_array[just_idx]
                        just_idx = right_child_idx
                    else:
                        break
        
        return returned_data
N=int(input())
h=Heap()
for _ in range(N):
    n=int(input())
    if n==0:
        p=h.pop()
        if p is None:
            print(0)
        else:
            print(p)
    else:
        h.insert(n)
        