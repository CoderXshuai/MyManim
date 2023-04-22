from manimlib import *


class FirstLinearTransformation(Scene):
    def construct(self):
        mob = Circle(color=PURPLE)
        mob.move_to(RIGHT + UP * 2)
        vector_array1 = np.array([[1], [2]])
        vector_array2 = np.array([[2], [1]])
        matrix = [[2, 0], [1, 1]]

        # self.add_transformable_mobject(mob)
        # self.add_vector(vector_array1, color=YELLOW)
        # self.add_vector(vector_array2, color=BLUE)
        # self.apply_matrix(matrix)
        self.wait(3)


class geometry(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-2, 2),
            y_range=(-2, 2)
        )
        axes.add_coordinate_labels()
        self.add(axes)
        colors = [BLUE, RED, GREEN]
        vectors = [
            np.array([2, 1]),
            np.array([1, 2]),
        ]
        dash = DashedLine(start=(3, 0, 0), end=(0, 3, 0))
        dash_tex = Tex("x_1-x_2", font_size=24)
        dash_tex.rotate(PI / 4, IN)
        dash_tex.move_to(UR * 1.7)
        line_1 = Line(start=[0.5, 1, 0], end=[0.5, 2.5, 0])
        line_2 = Line(start=[0.3, 0.6, 0], end=[2.5, 0.5, 0])
        for index, v in enumerate(vectors):
            temp_vec = Vector(
                direction=v,
                fill_color=colors[index % len(colors)],
            )
            temp_text = Tex(f"x{index + 1}({v[0]}, {v[1]})", font_size=24)
            self.add(temp_text)
            self.add(temp_vec)
            temp_text.move_to(np.hstack((v, 0)) * 1.2)
        self.add(dash)
        self.add(dash_tex)
        self.play(Write(line_1))
        self.play(FadeOut(line_1))
        self.add(line_2)


class LinearCombination(Scene):
    def construct(self):
        # 定义两个向量
        vectors = [
            np.array([2, 1]),
            np.array([1, 2]),
        ]
        # 公式描述内容
        description = VGroup(
            Text("linear combination"),
            Tex("x^1, \cdots, x^k \in \mathbb{R}^n,\\alpha_1, \cdots, \\alpha_k \in \mathbb{R},y=\sum_{i=1}^k \\alpha_i x^i"),
        )
        description.arrange(DOWN, buff=0.3)
        # 向量和标识集合
        content = VGroup(
        )
        # 描述信息置于最上方
        description.to_edge(UP)
        # 描述信息播放
        self.play(Write(description, run_time=1))
        # 向量和向量标识
        temp_vec, temp_text = None, None
        for index, v in enumerate(vectors):
            temp_vec = Vector(
                direction=v,
            )
            temp_text = Tex(f"x_{index + 1}({v[0]}, {v[1]})", font_size=24)
            content.add(temp_text)
            content.add(temp_vec)
            # 设置标识内容放置地方
            temp_text.move_to(np.hstack((v, 0)) * 1.2)
        # 表示可取的向量示例
        line_1 = Line(start=[0, 0, 0], end=[3, 3, 0])
        content.add(line_1)
        # 移动内容
        content.shift(DL * 2)
        content.remove(line_1)
        # 播放
        self.play(Write(content))
        self.play(Write(line_1), run_time=3)
        self.play(FadeOut(line_1))


class AffineCombination(Scene):
    def construct(self):
        vectors = [
            np.array([2, 1]),
            np.array([1, 2]),
        ]
        # 虚线封闭区域
        dash = DashedLine(start=(3, 0, 0), end=(0, 3, 0))
        dash_tex = Tex("x_1-x_2", font_size=24)
        # x1-x2向量文字
        dash_tex.rotate(PI / 4, IN)
        dash_tex.move_to(UR * 1.7)
        # 可取值向量示例
        line_1 = Line(start=[0, 0, 0], end=[0.5, 2.5, 0])
        line_2 = Line(start=[0, 0, 0], end=[1.5, 1.5, 0])
        line_3 = Line(start=[0, 0, 0], end=[2.5, 0.5, 0])

        description = VGroup(
            Text("affine combination"),
            Tex("x^1, \cdots, x^k \in \mathbb{R}^n,\\alpha_1, \cdots, \\alpha_k \in \mathbb{R},y=\sum_{i=1}^k \\alpha_i x^i, \sum_{i=1}^k \\alpha_i=1"),

        )
        description.arrange(DOWN, buff=0.3)
        content = VGroup(

        )
        description.to_edge(UP)
        self.add(description)
        temp_vec, temp_text = None, None
        for index, v in enumerate(vectors):
            temp_vec = Vector(
                direction=v,
            )
            temp_text = Tex(f"x_{index + 1}({v[0]}, {v[1]})", font_size=24)
            content.add(temp_text)
            content.add(temp_vec)
            temp_text.move_to(np.hstack((v, 0)) * 1.2)
        content.add(dash)
        content.add(dash_tex)
        content.add(line_1)
        content.add(line_2)
        content.add(line_3)
        content.shift(DL * 3)
        content.shift(LEFT * 3)
        content.shift(UP)
        content.remove(line_1)
        content.remove(line_2)
        content.remove(line_3)
        change = VGroup(
            Tex("y=\\alpha_1 x_1+\left(1-\\alpha_1\\right) x_2"),
            Tex("y=\\alpha_1\left(x_1-x_2\\right)+x_2"),
        )
        change.next_to(description, direction=DOWN)
        change.arrange(DOWN, buff=0.3)
        self.play(Write(change))
        self.play(Write(content))
        self.play(Write(line_1), run_time=3)
        self.play(FadeOut(line_1))
        self.play(Write(line_2), run_time=3)
        self.play(FadeOut(line_2))
        self.play(Write(line_3), run_time=3)
        self.play(FadeOut(line_3))


class ConvexCombination(Scene):
    def construct(self):
        vectors = [
            np.array([2, 1]),
            np.array([1, 2]),
        ]
        # 虚线封闭区域
        dash = DashedLine(start=(3, 0, 0), end=(0, 3, 0))
        dash_tex = Tex("x_1-x_2", font_size=24)
        # x1-x2向量文字
        dash_tex.rotate(PI / 4, IN)
        dash_tex.move_to(UR * 1.7)
        # 可取值向量示例
        line_1 = Line(start=[0, 0, 0], end=[1.5, 1.5, 0])
        description = VGroup(
            Text("convex combination"),
            Tex("x^1, \cdots, x^k \in \mathbb{R}^n,y=\sum_{i=1}^k \\alpha_i x^i, \\alpha_1, \cdots, \\alpha_k \geqslant 0,\sum_{i=1}^k \\alpha_i=1"),

        )
        description.arrange(DOWN, buff=0.3)
        content = VGroup(

        )
        description.to_edge(UP)
        self.add(description)
        temp_vec, temp_text = None, None
        for index, v in enumerate(vectors):
            temp_vec = Vector(
                direction=v,
            )
            temp_text = Tex(f"x_{index + 1}({v[0]}, {v[1]})", font_size=24)
            content.add(temp_text)
            content.add(temp_vec)
            temp_text.move_to(np.hstack((v, 0)) * 1.2)
        content.add(dash)
        content.add(dash_tex)
        content.add(line_1)
        content.shift(DL * 3)
        content.shift(LEFT * 3)
        content.shift(UP)
        content.remove(line_1)
        # condition = Tex("")
        change = VGroup(
            Tex("y=\\alpha_1 x_1+\left(1-\\alpha_1\\right) x_2"),
            Tex("y=\\alpha_1\left(x_1-x_2\\right)+x_2"),
        )
        # condition.next_to(description, aligned_edge=DOWN)
        change.next_to(description, direction=DOWN)
        change.arrange(DOWN, buff=0.3)
        # self.play(Write(condition))
        self.play(Write(change))
        self.play(Write(content))
        self.play(Write(line_1), run_time=3)
        self.play(FadeOut(line_1))


class GraphExample(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: 2 * math.sin(x),
            color=BLUE,
        )
        # By default, it draws it so as to somewhat smoothly interpolate
        # between sampled points (x, f(x)).  If the graph is meant to have
        # a corner, though, you can set use_smoothing to False
        relu_graph = axes.get_graph(
            lambda x: max(x, 0),
            use_smoothing=False,
            color=YELLOW,
        )
        # For discontinuous functions, you can specify the point of
        # discontinuity so that it does not try to draw over the gap.
        step_graph = axes.get_graph(
            lambda x: 2.0 if x > 3 else 1.0,
            discontinuities=[3],
            color=GREEN,
        )

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
        step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)

        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sin_graph, relu_graph),
            FadeTransform(sin_label, relu_label),
        )
        self.wait()
        self.play(
            ReplacementTransform(relu_graph, step_graph),
            FadeTransform(relu_label, step_label),
        )
        self.wait()

        parabola = axes.get_graph(lambda x: 0.25 * x ** 2)
        parabola.set_stroke(BLUE)
        self.play(
            FadeOut(step_graph),
            FadeOut(step_label),
            ShowCreation(parabola)
        )
        self.wait()

        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()


# n=2时 Non-negative Orthant example
class NonNegativeOrthant(Scene):
    def construct(self):
        # 创建标题
        text = Text("Non-negative Orthant")
        text.to_edge(UP)
        self.add(text)
        # 创建坐标轴并设置参数
        axes = Axes(
            x_range=[0, 6],
            y_range=[0, 6],
            x_length=8,
            y_length=8,
            axis_config={
                "numbers_to_include": range(6),
                "color": WHITE,
                "stroke_width": 2,
                "decimal_number_config": {"num_decimal_places": 0},
            },
            x_axis_config={"numbers_with_elongated_ticks": range(6)},
            y_axis_config={"numbers_with_elongated_ticks": range(6)},
        )
        # 播放坐标轴
        self.play(Write(axes))
        # 创建非负半轴
        orthant = Polygon(
            axes.c2p(0, 0),
            axes.c2p(0, 6),
            axes.c2p(6, 6),
            axes.c2p(6, 0),
            stroke_color=None,
            stroke_width=None,
            fill_color=RED,
            fill_opacity=0.2,
            stroke_opacity=0.8,
        )
        content = VGroup()
        content.add(axes, orthant)
        content.next_to(text, direction=DOWN)
        # 播放非负半轴
        self.add(orthant)
        tex = Tex(r"\mathbb{R}_{+}^n=\left\{x \in \mathbb{R}^n: x_i \geqslant 0 \right\}")
        word = Text("R=2")
        word.next_to(tex, direction=DOWN)
        # tex和word渲染
        self.play(Write(tex))
        self.play(Write(word))


class Hyperplane(Scene):
    def construct(self):
        # 创建 2D 坐标系
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            x_length=10,
            y_length=10,
            axis_config={
                "numbers_to_include": range(-5, 6),
                "color": WHITE,
                "stroke_width": 2,
                "decimal_number_config": {"num_decimal_places": 0},
            },
            x_axis_config={"numbers_with_elongated_ticks": range(-5, 6)},
            y_axis_config={"numbers_with_elongated_ticks": range(-5, 6)},
        )
        self.play(Write(axes))

        # 创建一个超平面
        hyperplane = Line(
            start=axes.c2p(-4, 4),
            end=axes.c2p(4, -4),
            stroke_color=RED,
            stroke_width=3,
        )
        self.play(Write(hyperplane))

        # 创建文本标签
        text = Tex(r"H: x_1 - 2x_2 + 3 = 0").next_to(hyperplane, direction=DOWN)
        self.play(Write(text))

        self.wait(2)
