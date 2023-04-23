from functools import reduce


class Staticsss ():
    def __init__(self, *nums) -> None:
        self.nums = sorted([*nums])

    def count(self):
        return len(self.nums)
    
    def sum(self):
        return reduce(lambda a,b: a+b, self.nums,0)

    def min(self):
        return self.nums[0]
    
    def max(self):
        return self.nums[-1]

    def range(self):
        return self.nums[-1] - self.nums[0]
    
    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        return self.nums[self.count()//2]
    
    def mode(self):
        return f'mode : {self.nums_occurrency()[0][0]} occurency : {self.nums_occurrency()[0][1]}'
    
    def standar_deviation(self):
        distance_from_mean_sqr =list(map(lambda a: (a - self.mean())*(a - self.mean()) ,self.nums))
        sum_distance_from_mean = reduce(lambda a,b : a+b, distance_from_mean_sqr, 0.0)
        return sum_distance_from_mean / self.count()
    
    def unique_nums(self):
        return set(self.nums)
    
    def nums_occurrency(self):
        return sorted([(num , self.nums.count(num)) for num in set(self.nums)],key=lambda a: a[1], reverse=True)
    
    def frequency_distribution(self):
        return [(self.nums.count(i)*100/self.count(), i) for i in list(self.unique_nums())]