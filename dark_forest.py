from manim import *
import numpy as np
import random

class DarkForestLaw(Scene):
    def construct(self):
        # 设置背景颜色为暗色宇宙
        self.camera.background_color = "#001122"
        
        # 标题
        self.title = Text("黑暗森林法则", font_size=48, color=YELLOW)
        self.play(Write(self.title))
        self.wait(1.5)
        self.play(self.title.animate.to_edge(UP))
        self.wait(0.5)
        
        # ================== 第一部分：基础公理 ==================
        # 基础公理标题
        axioms_title = Text("基础公理", font_size=36, color=GREEN)
        axioms_title.next_to(self.title, DOWN, buff=0.5)
        self.play(Write(axioms_title))
        self.wait(0.5)
        
        # 公理1：生存是第一需要
        axiom1 = VGroup()
        # 创建盾牌图标
        shield = Polygon(
            [0, 1, 0], [-1, -0.5, 0], [0, -0.2, 0], [1, -0.5, 0],
            color=GREEN, fill_opacity=0.3
        )
        shield.scale(0.5)
        # 创建文字
        text1 = Text("生存是文明的第一需要", font_size=28, color=GREEN)
        text1.next_to(shield, RIGHT, buff=0.5)
        axiom1.add(shield, text1)
        axiom1.next_to(axioms_title, DOWN, buff=0.8)
        
        # 公理2：资源有限
        axiom2 = VGroup()
        # 创建资源图标
        resources = VGroup()
        for i in range(5):
            dot = Dot(radius=0.1, color=TEAL)
            dot.move_to([-0.5 + i*0.25, 0, 0])
            resources.add(dot)
        # 创建增长箭头
        growth_arrow = Arrow(LEFT, RIGHT, color=YELLOW, buff=0.1)
        growth_arrow.scale(0.8)
        # 创建禁止符号
        stop_circle = Circle(radius=0.4, color=RED)
        stop_line1 = Line(UL, DR, color=RED, stroke_width=3)
        stop_line2 = Line(UR, DL, color=RED, stroke_width=3)
        stop_symbol = VGroup(stop_circle, stop_line1, stop_line2)
        stop_symbol.scale(0.3)
        stop_symbol.move_to(growth_arrow.get_end() + RIGHT * 0.7)
        # 创建文字
        text2 = Text("文明增长无限，但宇宙资源有限", font_size=28, color=GREEN)
        text2.next_to(resources, RIGHT, buff=1.0)
        axiom2.add(resources, growth_arrow, stop_symbol, text2)
        axiom2.next_to(axiom1, DOWN, buff=0.8)
        
        self.play(FadeIn(axiom1))
        self.wait(1)
        self.play(FadeIn(axiom2))
        self.wait(2)
        
        # 清屏（只保留标题）
        self.play(
            LaggedStart(
                FadeOut(axioms_title),
                FadeOut(axiom1),
                FadeOut(axiom2),
                lag_ratio=0.3,
                run_time=1.5
            )
        )
        self.wait(0.5)
        
        # ================== 第二部分：核心概念 ==================
        # 核心概念标题
        concepts_title = Text("核心概念", font_size=36, color=BLUE)
        concepts_title.next_to(self.title, DOWN, buff=0.5)
        self.play(Write(concepts_title))
        self.wait(0.5)
        
        # 概念1：技术爆炸
        concept1 = VGroup()
        # 创建爆炸图标
        explosion = VGroup()
        for i in range(8):
            line = Line(ORIGIN, UP * 0.5, color=YELLOW, stroke_width=2)
            line.rotate(i * PI / 4)
            explosion.add(line)
        explosion.scale(0.8)
        # 创建指数曲线
        curve = ParametricFunction(
            lambda t: np.array([t, np.exp(t - 1.5) - 0.5, 0]),
            t_range=[0, 3],
            color=ORANGE
        )
        curve.scale(0.4).next_to(explosion, RIGHT, buff=0.3)
        # 创建文字
        text3 = Text("技术爆炸", font_size=28, color=BLUE)
        text3.next_to(curve, RIGHT, buff=0.5)
        concept1.add(explosion, curve, text3)
        concept1.next_to(concepts_title, DOWN, buff=0.8)
        
        # 概念2：猜疑链
        concept2 = VGroup()
        # 创建两个文明点
        civ1 = Dot(color=RED)
        civ2 = Dot(color=BLUE)
        civ2.next_to(civ1, RIGHT, buff=1.5)
        # 创建猜疑箭头
        arrow1 = Arrow(civ1.get_right(), civ1.get_right() + RIGHT*0.7, 
                      color=RED, buff=0.1, tip_length=0.2)
        arrow2 = Arrow(civ2.get_left(), civ2.get_left() + LEFT*0.7, 
                      color=BLUE, buff=0.1, tip_length=0.2)
        # 创建问号
        question1 = Text("?", color=RED, font_size=30).next_to(arrow1, UP, buff=0.1)
        question2 = Text("?", color=BLUE, font_size=30).next_to(arrow2, UP, buff=0.1)
        # 创建文字
        text4 = Text("猜疑链", font_size=28, color=BLUE)
        text4.next_to(civ2, RIGHT, buff=0.5)
        concept2.add(civ1, civ2, arrow1, arrow2, question1, question2, text4)
        concept2.next_to(concept1, DOWN, buff=0.8)
        
        # 确保概念2在屏幕范围内
        if concept2.get_bottom()[1] < -config.frame_height/2 + 0.5:
            concept2.shift(UP * 1.5)
        
        self.play(FadeIn(concept1))
        self.wait(1)
        self.play(FadeIn(concept2))
        self.wait(3)
        
        # 清屏（只保留标题）
        self.play(
            LaggedStart(
                FadeOut(concepts_title),
                FadeOut(concept1),
                FadeOut(concept2),
                lag_ratio=0.3,
                run_time=1.5
            )
        )
        self.wait(0.5)
        
        # ================== 第三部分：法则原文和动画演示 ==================
        # 法则原文
        quote = Text(
            "宇宙就是一座黑暗森林，每个文明都是带枪的猎人，\n"
            "像幽灵般潜行于林间，轻轻拨开挡路的树枝，\n"
            "竭力不让脚步发出一点儿声音，连呼吸都必须小心翼翼……\n"
            "他必须小心，因为林中到处都有与他一样潜行的猎人。\n"
            "如果他发现了别的生命，能做的只有一件事：开枪消灭之。",
            font_size=24,
            color=BLUE_B,
            line_spacing=1.2
        )
        quote.next_to(self.title, DOWN, buff=0.5)
        self.play(Write(quote), run_time=4)
        self.wait(3)
        self.play(FadeOut(quote))
        
        # 创建宇宙森林
        self.create_cosmic_forest()
        
        # 展示文明点
        civilizations = self.create_civilizations(15)
        self.play(LaggedStartMap(FadeIn, civilizations, lag_ratio=0.1))
        self.wait()
        
        # 展示技术爆炸概念
        self.tech_explosion(civilizations[0])
        
        # 展示猜疑链
        self.chain_of_suspicion(civilizations[1], civilizations[2])
        
        # 展示黑暗森林打击
        self.dark_forest_strike(civilizations[3])
        
        # 结论
        conclusion = Text(
            "在黑暗森林中，暴露自己位置等于自取灭亡\n"
            "保持沉默是宇宙文明生存的唯一选择",
            font_size=36,
            color=RED,
            weight=BOLD
        )
        conclusion.set_y(-2)
        self.play(Write(conclusion))
        self.wait(3)
        
    def create_cosmic_forest(self):
        """创建宇宙森林背景"""
        # 添加背景星星
        stars = VGroup()
        for _ in range(100):
            star = Dot(
                point=np.array([
                    (np.random.random() - 0.5) * config.frame_width,
                    (np.random.random() - 0.5) * config.frame_height,
                    0
                ]),
                radius=np.random.random() * 0.03,
                color=WHITE
            )
            star.set_opacity(np.random.random() * 0.7 + 0.3)
            stars.add(star)
        
        # 添加一些星云
        nebulae = VGroup()
        colors = [BLUE_E, PURPLE_E, TEAL_E, MAROON_E]
        for _ in range(4):
            nebula = Dot(
                point=np.array([
                    (np.random.random() - 0.5) * config.frame_width * 0.8,
                    (np.random.random() - 0.5) * config.frame_height * 0.8,
                    0
                ]),
                radius=np.random.random() * 1.5 + 0.5,
                color=random.choice(colors)
            )
            nebula.set_opacity(0.15)
            nebulae.add(nebula)
        
        self.add(stars, nebulae)
        
    def create_civilizations(self, n):
        """创建文明点"""
        civilizations = VGroup()
        colors = [YELLOW, RED, GREEN, BLUE, ORANGE, PINK]
        
        for i in range(n):
            # 随机位置但避免重叠
            while True:
                x = (np.random.random() - 0.5) * config.frame_width * 0.8
                y = (np.random.random() - 0.5) * config.frame_height * 0.6
                pos = np.array([x, y, 0])
                
                # 检查是否与其他文明太近
                too_close = False
                for civ in civilizations:
                    if np.linalg.norm(pos - civ.get_center()) < 1.0:
                        too_close = True
                        break
                
                if not too_close:
                    break
            
            # 创建文明点
            civ = VGroup()
            
            # 核心点
            core = Dot(point=pos, color=random.choice(colors), radius=0.15)
            
            # 光环
            halo = Circle(radius=0.3, color=core.get_color(), fill_opacity=0.1)
            halo.move_to(pos)
            
            civ.add(core, halo)
            civilizations.add(civ)
        
        return civilizations
    
    def tech_explosion(self, civilization):
        """展示技术爆炸概念"""
        civ_copy = civilization.copy()
        self.play(civ_copy.animate.scale(1.5).set_color(YELLOW), run_time=0.5)
        
        # 添加技术爆炸标签
        label = Text("技术爆炸", font_size=24, color=YELLOW)
        label.next_to(civ_copy, UP, buff=0.3)
        
        # 添加指数增长曲线
        curve = ParametricFunction(
            lambda t: np.array([
                t,
                np.exp(t - 2) - 1,
                0
            ]),
            t_range=[0, 4],
            color=YELLOW
        )
        curve.scale(0.5).next_to(civ_copy, DOWN, buff=0.5)
        
        self.play(Write(label), Create(curve), run_time=1.5)
        self.wait(2)
        
        # 移除临时对象
        self.play(
            FadeOut(civ_copy),
            FadeOut(label),
            FadeOut(curve)
        )
    
    def chain_of_suspicion(self, civ1, civ2):
        """展示猜疑链"""
        # 突出显示两个文明
        self.play(
            civ1.animate.set_color(RED).scale(1.3),
            civ2.animate.set_color(BLUE).scale(1.3)
        )
        
        # 添加标签
        label1 = Text("文明A", font_size=20, color=RED)
        label1.next_to(civ1, DOWN, buff=0.2)
        
        label2 = Text("文明B", font_size=20, color=BLUE)
        label2.next_to(civ2, DOWN, buff=0.2)
        
        self.play(Write(label1), Write(label2))
        self.wait(0.5)
        
        # 创建猜疑链
        thoughts = VGroup()
        texts = [
            "对方是善意的吗？",
            "对方认为我是善意的吗？",
            "对方认为我认为他是善意的吗？",
            "对方会先攻击吗？"
        ]
        
        # 文明A的思考
        for i, text in enumerate(texts):
            thought = Text(text, font_size=20, color=RED)
            thought.next_to(civ1, LEFT if i % 2 == 0 else RIGHT, buff=0.5)
            thought.shift(UP * i * 0.5)
            thoughts.add(thought)
        
        # 文明B的思考
        for i, text in enumerate(texts):
            thought = Text(text, font_size=20, color=BLUE)
            thought.next_to(civ2, RIGHT if i % 2 == 0 else LEFT, buff=0.5)
            thought.shift(UP * i * 0.5)
            thoughts.add(thought)
        
        self.play(LaggedStartMap(FadeIn, thoughts, lag_ratio=0.2), run_time=3)
        self.wait(2)
        
        # 结论
        conclusion = Text("无法建立信任 → 先发制人", font_size=24, color=YELLOW)
        conclusion.move_to((civ1.get_center() + civ2.get_center()) / 2)
        conclusion.shift(DOWN * 1.5)
        
        self.play(Write(conclusion))
        self.wait(2)
        
        # 恢复原状
        self.play(
            FadeOut(thoughts),
            FadeOut(label1),
            FadeOut(label2),
            FadeOut(conclusion),
            civ1.animate.set_color(WHITE).scale(1/1.3),
            civ2.animate.set_color(WHITE).scale(1/1.3)
        )
    
    def dark_forest_strike(self, civilization):
        """展示黑暗森林打击"""
        # 突出目标文明
        self.play(civilization.animate.set_color(YELLOW).scale(1.5))
        
        # 添加"暴露位置"标签
        expose_label = Text("暴露位置", font_size=24, color=YELLOW)
        expose_label.next_to(civilization, UP, buff=0.3)
        self.play(Write(expose_label))
        self.wait(1)
        
        # 显示来自其他方向的攻击
        attackers = VGroup()
        directions = [UP, DOWN, LEFT, RIGHT, UR, UL, DR, DL]
        for direction in directions:
            attacker = Triangle(color=RED, fill_opacity=0.8)
            attacker.scale(0.2)
            # Check if direction is LEFT or RIGHT using array comparison
            is_horizontal = np.array_equal(direction, LEFT) or np.array_equal(direction, RIGHT)
            attacker.rotate(PI/2 if is_horizontal else 0)
            attacker.move_to(civilization.get_center() + direction * 3)
            attackers.add(attacker)
        
        self.play(LaggedStartMap(FadeIn, attackers, lag_ratio=0.1))
        self.wait(0.5)
        
        # 攻击动画
        attack_lines = VGroup()
        for attacker in attackers:
            line = Line(
                attacker.get_center(),
                civilization.get_center(),
                color=RED,
                stroke_width=3
            )
            attack_lines.add(line)
        
        self.play(
            LaggedStartMap(
                Create, attack_lines, 
                lag_ratio=0.1,
                run_time=1.5
            )
        )
        
        # 打击效果
        explosion = VGroup()
        for i in range(20):
            line = Line(ORIGIN, UP * 0.5, color=YELLOW, stroke_width=3)
            line.rotate(i * PI / 10)
            explosion.add(line)
        explosion.move_to(civilization.get_center())
        
        self.play(
            FadeOut(civilization),
            FadeIn(explosion.scale(0.5))
        )

        self.play(
            explosion.animate.scale(3).set_opacity(0),
            run_time=1.5
        )
        
        # 移除攻击者
        self.play(
            FadeOut(attackers),
            FadeOut(attack_lines),
            FadeOut(expose_label)
        )
        
        # 添加打击结论
        strike_text = Text("黑暗森林打击", font_size=28, color=RED)
        strike_text.move_to(civilization.get_center())
        self.play(Write(strike_text))
        self.wait(2)
        self.play(FadeOut(strike_text))
        
        # 清屏并显示结束语
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != self.title])
        self.wait(0.5)
        
        # 结束语
        ending = Text(
            "在宇宙的黑暗森林中\n每个文明都是孤独的猎人\n\n保持沉默\n或许是我们唯一的生存之道",
            font_size=32,
            color=LIGHT_GREY,
            line_spacing=1.2
        )
        self.play(Write(ending), run_time=3)
        self.wait(3)
        
        # 最终淡出
        self.play(FadeOut(ending), run_time=2)