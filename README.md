# tiny graph

![image](https://github.com/zideajang/tiny_graph/blob/main/assets/flow_control.png)

## 安装

```
pip install -e .
```

## 快速入门
![image](https://github.com/zideajang/tiny_graph/blob/main/assets/simple_chain.PNG)

### 定义节点
```python
class AddComp(Component):

    def run(self,input):
        self.context = {
            "input":input,
            "output":input + 1
        }
        return input + 1
```
- 定义 Component 类
- 需要实现一下 `run` 这个抽象方法
### 构建计算图
对一个简单图是包括节点和节点之间的边
- 定义一个图
```python
simple_graph = SimpleGraph("simple_chain")
```
- 添加节点
```python
add_one_comp = AddComp("add_1")
mul_two_comp = MulComp("mul_1")
```
- 添加节点之间的边
```python
simple_graph.add_connect(add_one_comp,mul_two_comp)
```
- 为图指定起始节点和结束节点
```python
simple_graph.start_comp_name = "add_1"
simple_graph.end_comp_name = "mul_1"
```

### 编译
- 随后可以通过指定不同遍历引擎实现不同编译
```python
simple_graph.compile("add_1")
```
### 运行

```python
res = simple_graph.run(2)
```