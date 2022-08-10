from manim import *

class sigmoid(ThreeDScene):
    def construct(self):
        #Defining the modals

        #<-------------- All details of first model ---------------------->

        m1 = Rectangle(height= 0.9, width= 2.7, fill_opacity= 1, fill_color= YELLOW, color= YELLOW).shift(UP*1.7)  #a rectangle
        m1_tex1 = Text("Model", color= BLUE).shift(m1.get_center())						                           #Model text inside rectangle
        internet = ImageMobject("internet.png").scale(0.5).shift(m1.get_top() + RIGHT * 1.6)		               #A picture of internet
        model1 = VGroup(m1, m1_tex1)										                                       #Grouping rectangle and model text
        m1_Q = Text("Is the internet\n   working?", color= BLUE, font_size= 25).shift(model1.get_left() + LEFT * 3.9)#Question Text
        m1_A = Text("No (0)", color= YELLOW, font_size= 25).shift(model1.get_right() + RIGHT * 4.6)			        #Answer Text
        m1_Qm1 = Arrow(start= m1_Q.get_right(), end= model1.get_left(), color= BLUE)			  		            #Question to model arrow
        m1_m1A = Arrow(start= model1.get_right(), end= m1_A.get_left(), color= YELLOW)			   	 	            #Model to answer arrow

	      #<xxxxxxxxxxxx  Model 1 details end xxxxxxxxxxxxxxxxxxxx>

	      #<-------------- All details of 2nd model ---------------------->

        m2 = Rectangle(height= 0.9, width= 2.7, fill_opacity= 1, fill_color= YELLOW, color= YELLOW).shift(DOWN*1.7)
        m2_tex1 = Text("Model", color= BLUE).shift(m2.get_center())
        car_crash = ImageMobject("car_crash.png").scale(0.5).shift(m2.get_top() + RIGHT * 1.8)
        model2 = VGroup(m2, m2_tex1)
        m2_Q = Text("Did he survive in\nthe accident?", color= BLUE, font_size= 25).shift(model2.get_left() + LEFT * 3.9)
        m2_A = Text("Yes (1)", color= YELLOW, font_size= 25).shift(model2.get_right() + RIGHT * 4.6)                     
        m2_Qm2 = Arrow(start= m2_Q.get_right(), end= model2.get_left(), color= BLUE)                                            
        m2_m2A = Arrow(start= model2.get_right(), end= m2_A.get_left(), color= YELLOW)

        #<xxxxxxxxxxxx  Model 2 details end xxxxxxxxxxxxxxxxxxxx>


	      #<------------ Describing the Probabilities Section ----------->
        probabilities = Text("Probabilities", font_size= 30).to_edge(UR).rotate(-PI/8)
        cross1 = Cross().scale(0.5).shift(m1_A.get_center())
        cross2 = Cross().scale(0.5).shift(m2_A.get_center())
        ptexm1 = Text("\t30%", color= YELLOW, font_size= 20).shift(model1.get_right() + RIGHT * 3.9)
        ptexm2 = Text("\t90%", color= YELLOW, font_size= 20).shift(model2.get_right() + RIGHT * 3.9) 
        
        self.play(Create(VGroup(model1, model2)))
        self.wait(3)
        self.play(Create(VGroup(m1_Q, m1_Qm1)), run_time= 2)
        self.wait(3)
        self.play(FadeIn(internet))
        self.play(Create(VGroup(m1_m1A, m1_A)), run_time= 3)
        self.wait(4)
        self.wait(2)
        self.play(Create(VGroup(m2_Q, m2_Qm2)), run_time= 2)
        self.wait(3)
        self.play(FadeIn(car_crash))
        self.play(Create(VGroup(m2_m2A, m2_A)), run_time= 3)
        self.play(Write(probabilities))
        self.wait(3)
        self.play(Create(VGroup(cross1, cross2)))        
        self.play(ReplacementTransform(VGroup(m1_A, m2_A), VGroup(ptexm1, ptexm2)), run_time= 3)
        self.wait(3)
        self.play(FadeOut(VGroup(model1, model2, m1_Q, m1_Qm1, m1_m1A, ptexm1, m2_Q, m2_Qm2, m2_m2A, ptexm2, probabilities, cross1, cross2)), run_time= 3)
        self.play(FadeOut(internet), run_time= 0.1)
        self.play(FadeOut(car_crash), run_time= 0.1)
        self.wait(2)


        #<----------------- Describing sigmoid function, plot it along with axes and further detail--------------->

        axes = Axes().add_coordinates()         #  xy-axes
        sigmoid_function_tex = MathTex(r"f(x)=\frac{a}{1+e^{-b(x-c)}}")
        sigmoid_function_tex1 = MathTex(r"f(x)=\frac{1}{1+e^{-x}}", color= YELLOW)
        parameters = Text("Where a, b and c are the parameters.", font_size= 25).shift(sigmoid_function_tex.get_top() + UP * 1)
        a_para = Text("Parameter a encodes the\nheight.\n(Default is 1)", font_size= 20).shift(sigmoid_function_tex.get_right()+ RIGHT * 3.1)
        b_para = Text("b encodes how fast the\nslope raises", font_size= 20).shift(sigmoid_function_tex.get_right()+ RIGHT * 3.1)
        c_para = Text("c controls the centre.", font_size= 20).shift(sigmoid_function_tex.get_center() + RIGHT * 4 )

        e = 2.71828182846  # the exponential variable e
        sigmoid_function = axes.plot(lambda x: 1/ ( 1 + e**(-x) ), color= YELLOW)

        poi = Dot(axes.c2p(0.8, 1/ (1 + e**(-0.8))), color= RED ) #Point of interest f(0.8) = xxxxx

        #self.add(axes, sigmoid_function)

        #<-----------Text information written on screen ------------>
        self.play(Write(sigmoid_function_tex))
        self.wait(3)              # Writes sigmoid function in text form
        self.play(Write(parameters), run_time= 3)   # Writes the parameter line
        self.wait(2)                                # Holds the video for 1 second
        self.play(Write(a_para), run_time= 3)       # Writes the a parameter line
        self.wait(3)
        self.play(FadeOut(a_para))                  # Fades out the a parameter line
        self.wait(1)
        self.play(Write(b_para), run_time= 3)
        self.wait(3)
        self.play(FadeOut(b_para))
        self.wait(1)
        self.play(Write(c_para), run_time= 3)
        self.wait(3)
        self.play(FadeOut(VGroup(parameters, c_para)))  #Fades out text from screen
        self.play(ReplacementTransform(sigmoid_function_tex, sigmoid_function_tex1), run_time= 2)  #Replaces the equation in parameter form to real form in which a=1, b=1, c=0
        self.play(sigmoid_function_tex1.animate.to_edge(UL))        #shifts the equation to the UP left corner of the screen
        self.wait(2)

        #<------------ Creating Axes, function and point of interest on the screen ------------>
        self.play(Create(axes), run_time= 1)                #Creates axes
        self.wait(2)
        self.play(Create(sigmoid_function), run_time= 3)    #Creates the function
        self.wait(3)
        self.play(Create(poi), run_time= 2)  #Creates Dot at point f(0.8)
        self.play(Create(Line(start= axes.c2p(0.8,0), end= axes.c2p(0.8, 1/ (1 + e**(-0.8))), color= RED))) #Creates a vertical line at x=0.8 ranging from y=0 to the red dot created above
        self.wait(1)
        self.play(Create(Line(start= axes.c2p(0,1/ (1 + e**(-0.8))), end= axes.c2p(0.8, 1/ (1 + e**(-0.8))), color= RED))) #Creates a vertical line at y=0.8 ranging from x=0 to the red dot created above
        self.wait(1)
        self.set_camera_orientation(zoom= 2)   #zooms in
        self.wait(2)
        self.play(Write(Text("(0.8,0.689)",font_size= 18, color= RED).next_to(poi, UP)))
        self.wait(3)
        self.set_camera_orientation(zoom= 1)   #zooms out
        self.play(Write(Text("69% chance the sample\nis in the positive\nclass when x = 0.8",color= RED, font_size= 20).to_edge(DL)))
        self.wait(2)
