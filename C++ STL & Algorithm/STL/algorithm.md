### **详细说明：`<algorithm>` 中常用操作**

以下是 `std::algorithm` 中的主要函数，详细介绍了其作用、参数范围（开闭区间）、返回值及示例。

---

### **1. 排序相关操作**

#### **1.1 `std::sort`**
- **作用**: 对指定范围内的元素进行升序排序（默认）。
- **区间**: `[first, last)`（左闭右开）。
- **返回值**: 无（就地排序）。
- **复杂度**: \(O(n \log n)\)。

```cpp
std::sort(vec.begin(), vec.end()); // 升序排序
std::sort(vec.begin(), vec.end(), std::greater<int>()); // 降序排序
```

---

#### **1.2 `std::stable_sort`**
- **作用**: 稳定排序，保持相等元素的相对顺序。
- **区间**: `[first, last)`。
- **返回值**: 无。
- **复杂度**: \(O(n \log^2 n)\)。

---

#### **1.3 `std::partial_sort`**
- **作用**: 仅对范围的前部分排序，适用于仅需获取前 \(k\) 个最小值的场景。
- **区间**: `[first, middle)` 为排序结果，`[middle, last)` 未定义顺序。
- **返回值**: 无。
- **复杂度**: \(O(n \log k)\)。

```cpp
std::partial_sort(vec.begin(), vec.begin() + k, vec.end());
```

---

#### **1.4 `std::nth_element`**
- **作用**: 找到第 \(n\) 小的元素，将其放在正确位置，前面的元素小于它，后面的元素大于它，但两部分顺序未定义。
- **区间**: `[first, last)`。
- **返回值**: 无。
- **复杂度**: 平均 \(O(n)\)。

```cpp
std::nth_element(vec.begin(), vec.begin() + n, vec.end());
```

---

### **2. 搜索相关操作**

#### **2.1 `std::find`**
- **作用**: 查找第一个等于指定值的元素。
- **区间**: `[first, last)`。
- **返回值**: 指向找到的元素的迭代器，未找到时返回 `last`。

```cpp
auto it = std::find(vec.begin(), vec.end(), value);
if (it != vec.end()) std::cout << "Found: " << *it;
```

---

#### **2.2 `std::binary_search`**
- **作用**: 使用二分法检查范围内是否存在值（需要排序）。
- **区间**: `[first, last)`。
- **返回值**: 布尔值，`true` 表示存在。

```cpp
bool found = std::binary_search(vec.begin(), vec.end(), value);
```

---

#### **2.3 `std::lower_bound` / `std::upper_bound`**
- **作用**: 在有序范围中查找值的上下边界。
  - `std::lower_bound`: 第一个 **不小于** 值的位置。
  - `std::upper_bound`: 第一个 **大于** 值的位置。
- **区间**: `[first, last)`。
- **返回值**: 指向对应位置的迭代器。

```cpp
auto lower = std::lower_bound(vec.begin(), vec.end(), value);
auto upper = std::upper_bound(vec.begin(), vec.end(), value);
```

---

### **3. 修改操作**

#### **3.1 `std::reverse`**
- **作用**: 反转范围内元素的顺序。
- **区间**: `[first, last)`。
- **返回值**: 无。

```cpp
std::reverse(vec.begin(), vec.end());
```

---

#### **3.2 `std::rotate`**
- **作用**: 将 `[first, middle)` 移动到 `[middle, last)` 之后。
- **区间**: `[first, last)`。
- **返回值**: 指向新范围的开始。

```cpp
std::rotate(vec.begin(), vec.begin() + k, vec.end());
```

---

#### **3.3 `std::unique`**
- **作用**: 删除相邻重复元素，返回新的范围结尾迭代器。
- **区间**: `[first, last)`。
- **返回值**: 新范围的结束迭代器。
- **注意**: 不会缩小容器大小，需配合 `erase` 使用。

```cpp
auto new_end = std::unique(vec.begin(), vec.end());
vec.erase(new_end, vec.end());
```

---

### **4. 计数操作**

#### **4.1 `std::count`**
- **作用**: 统计范围内某值出现的次数。
- **区间**: `[first, last)`。
- **返回值**: 元素出现的次数。

```cpp
int cnt = std::count(vec.begin(), vec.end(), value);
```

---

#### **4.2 `std::count_if`**
- **作用**: 统计满足条件的元素个数。
- **区间**: `[first, last)`。
- **返回值**: 满足条件的元素个数。

```cpp
int cnt = std::count_if(vec.begin(), vec.end(), [](int x) { return x > 0; });
```

---

### **5. 集合操作** (适用于有序范围)

#### **5.1 `std::set_union`**
- **作用**: 计算两个有序范围的并集。
- **区间**: `[first1, last1)` 和 `[first2, last2)`。
- **返回值**: 指向输出范围的结束迭代器。

```cpp
std::vector<int> result(vec1.size() + vec2.size());
auto it = std::set_union(vec1.begin(), vec1.end(), vec2.begin(), vec2.end(), result.begin());
result.resize(it - result.begin());
```

#### **5.2 `std::set_intersection`**
- **作用**: 计算两个有序范围的交集。

---

### **6. 数学相关操作**

#### **6.1 `std::accumulate`**
- **作用**: 求范围内所有元素的累计和。
- **区间**: `[first, last)`。
- **返回值**: 累计值。
- **注意**: 需包含头文件 `<numeric>`。

```cpp
#include <numeric>
int sum = std::accumulate(vec.begin(), vec.end(), 0);
```

---

### **总结表格**

| 函数名              | 功能                       | 区间             | 返回值                  |
|---------------------|----------------------------|------------------|-------------------------|
| `std::sort`         | 升序排序                  | `[first, last)`  | 无                      |
| `std::reverse`      | 反转范围                  | `[first, last)`  | 无                      |
| `std::find`         | 查找第一个匹配值          | `[first, last)`  | 匹配值的迭代器          |
| `std::count`        | 统计值出现次数            | `[first, last)`  | 值出现的次数            |
| `std::accumulate`   | 累加求和                  | `[first, last)`  | 总和                    |
| `std::unique`       | 去除相邻重复值            | `[first, last)`  | 新的范围结束迭代器      |

希望这些详细信息能让你对 `<algorithm>` 的使用更加得心应手！ 😊