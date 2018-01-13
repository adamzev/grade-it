class DrawProblem:
    def __init__(self):
        pass

    @staticmethod
    def drawBasicOpProblem(prob_rect, problem, pdfCanvas, orientation):
        if orientation not in ['vert', 'horiz']:
            raise ValueError("Unsupported Orientation Type: Must be \"vert\", or \"horiz\"")
        if orientation == 'vert':
            DrawProblem.drawVertBasicOpProblem(prob_rect, problem, pdfCanvas)
        elif orientation == 'horiz':
            DrawProblem.drawHorizBasicOpProblem(prob_rect, problem, pdfCanvas)

    @staticmethod
    def drawVertBasicOpProblem(prob_rect, problem, pdfCanvas):
        h_font_size = 14 # heading font size
        p_font_size = 16 # problem font size
        p_char_spacing = p_font_size
        cnv = pdfCanvas.c
        top_of_page = 10 * pdfCanvas.inch
        line_size = p_char_spacing

        num1 = str(problem.num1)
        num2 = str(problem.num2)
        # TODO: replace this with right allign 
        if len(num1) == 1:
            num1 = " " + num1
        if len(num2) == 1:
            num2 = " " + num2
                        
        cnv.drawString(prob_rect[0] + p_char_spacing * 4, prob_rect[1], num1 )
        

        cnv.drawString(prob_rect[0] + p_char_spacing * 4, prob_rect[1] - line_size * 1, num2)
        cnv.drawString(prob_rect[0] + p_char_spacing * 3, prob_rect[1] - line_size * 1, problem.op_symbol)
        cnv.line(prob_rect[0] + p_char_spacing * 2.8, prob_rect[1] - line_size * 1.2, prob_rect[0] + p_char_spacing * 5.3, prob_rect[1] - line_size * 1.2)

    @staticmethod
    def drawHorizBasicOpProblem(prob_rect, problem, pdfCanvas):
        pass
