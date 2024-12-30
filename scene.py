from manim import *

class Scene1(Scene):
    def construct(self):
        formula_1 = MathTex("(a + b)^2", font_size=72, color=YELLOW)
        # formula_1.move_to(ORIGIN)
        self.play(Write(formula_1))
        self.wait(5)

        formula_2 = MathTex(
            "(a + b)^2", "=", "a^2", "+", "2ab", "+", "b^2", font_size=72
        )
        
        formula_2[2].set_color(BLUE)   # a^2
        formula_2[4].set_color(ORANGE)  # 2ab
        formula_2[6].set_color(GREEN)  # b^2

        formula_2.move_to(ORIGIN)
        self.play(Transform(formula_1, formula_2))
        self.wait(5)

        self.play(Indicate(formula_2[2]))  # Highlight a^2
        self.wait(2)

        self.play(Indicate(formula_2[4]))  # Highlight 2ab
        self.wait(2)

        self.play(Indicate(formula_2[6]))  # Highlight b^2
        self.wait(2)

        self.play(FadeOut(formula_2, run_time=2))
        self.wait(2)

class Scene2(Scene):
    def construct(self):

        formula_2 = MathTex(
            "(a + b)^2", "=", "a^2", "+", "2ab", "+", "b^2", font_size=72
        )

        formula_2[2].set_color(BLUE)   # a^2
        formula_2[4].set_color(ORANGE)  # 2ab
        formula_2[6].set_color(GREEN)  # b^2

        self.add(formula_2)
        self.wait(1)
    
        formula_3 = MathTex(
            "b^2", "=", "b", "*", "b", font_size=75
        )

        formula_3[0].set_color(GREEN)
        formula_3[2].set_color(BLUE)
        formula_3[4].set_color(BLUE)

        formula_3.move_to(ORIGIN)
        # Use Transform with the removal of previous object (formula_2)
        self.play(Transform(formula_2, formula_3))  
        self.wait(5)

class Scene3(Scene):
    def construct(self):

        formula_3= MathTex(
            "(a + b)^2", "=", "a^2", "+", "2ab", "+", "b^2", font_size=72
        )

        formula_3[2].set_color(BLUE)   # a^2
        formula_3[4].set_color(ORANGE)  # 2ab
        formula_3[6].set_color(GREEN)  # b^2

        formula_3.move_to(ORIGIN)
        # Use Transform with the removal of previous object (formula_2)
        self.add(formula_3)
        self.wait(1)

        # Now formula_3 should be replaced by formula_4. Let's remove formula_3 after this
        formula_4 = MathTex(
            "2ab", "=", "2", "*", "a", "*", "b", font_size=75
        )

        formula_4[0].set_color(ORANGE)
        formula_4[2].set_color(ORANGE)
        formula_4[4].set_color(ORANGE)
        formula_4[6].set_color(ORANGE)
        
        formula_4.move_to(ORIGIN)
        # Remove the previous formula (formula_3) before playing the transition
        self.play(ReplacementTransform(formula_3, formula_4))
        self.wait(1)

        

