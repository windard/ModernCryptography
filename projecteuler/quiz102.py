# coding=utf-8

# how to check a point inside of a triangle

# 叉乘
# A(x1, y1) ^ B(x2, y2) = x1y2 - x2y1

# 1. 计算面积
# ![](https://windard-blog.oss-cn-beijing.aliyuncs.com/1607871592119.png) 
# 叉乘的绝对值即为向量交叉平行四边形的面积

def calculate_area(a, b, c):
	return 0.5 * abs((a[0]-b[0])*(a[1]-c[1]) - (a[0]-c[0])*(a[1]-b[1]))


def check_point_area_inside_triangle(point, a, b, c):
	return calculate_area(a, b, c) == (
			calculate_area(point, a, b) + calculate_area(point, a, c) + calculate_area(point, b, c)
		)


# 2. 同侧法
# ![](https://windard-blog.oss-cn-beijing.aliyuncs.com/1607876906426.png)
# 以 AB 未例，如果 AM*AB>0, AN*AB>0 则M 和 N 在同侧，AO<0 则 O 与 M,N 在异侧

def calculate_sign(a, b, c):
	return (a[0]-c[0])*(b[1]-c[1]) - (b[0]-c[0])*(a[1]-c[1])


def calculate_same_side(a, b, m, n):
	return calculate_sign(a, b, m) * calculate_sign(a, b, n) >= 0
	# 此处不能直接比较布尔值，因为负数的布尔值也为正
	# return bool(calculate_sign(a, b, m)) == bool(calculate_sign(a, b, n) )


def check_point_same_side_inside_triangle(point, a, b, c):
	return calculate_same_side(a, b, c, point) and calculate_same_side(a, c, b, point) and calculate_same_side(b, c, a, point)

# 3. 内角和
# 三角形内角和360度，每个内角都不能大于180度
# 叉乘的向量结果是有顺序的，PA^PB 的叉乘结果为正 表示两个向量的夹角在逆时针180°以内，即 PA 与 PB 的夹角在逆时针 180° 以内
# 所以如果叉乘的向量结果为负，说明交叉角度在顺时针 180° 以上，或者顺时针 180° 以内。


def check_point_angle_inside_triangle(point, a, b, c):
	pab = calculate_sign(point, a, b)
	pbc = calculate_sign(point, b, c)
	pca = calculate_sign(point, c, a)
	return all(map(lambda x: x >= 0, [pab, pbc, pca])) or all(map(lambda x: x <= 0, [pab, pbc, pca]))


if __name__ == '__main__':
	print(check_point_angle_inside_triangle((0,0), (-340,495), (-153,-910), (835,-947)))
	print(check_point_angle_inside_triangle((0,0), (-175,41), (-421,-714), (574,-645)))
	count = 0
	with open("p102_triangles.txt", "r") as f:
		line = f.readline()
		while line:
			nums = list(map(int, line.strip().split(',')))
			if check_point_same_side_inside_triangle((0,0), (nums[0], nums[1]), (nums[2], nums[3]), (nums[4], nums[5])):
				count += 1
			line = f.readline()

	print(count)
