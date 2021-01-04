import data_and_func as d




answers1 = [d.AnswerBlocks(['True'], point=1, score=1,),
            d.AnswerBlocks(['False'], point=1, score=1,),
            d.AnswerBlocks(['Yes'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['Lie'], point=0, score=-1, life=-1)
            ]

question1 = d.Questions(2,["Eat all boolean values",])



answers2 = [d.AnswerBlocks(['list'], point=1, score=1,),
            d.AnswerBlocks(['float'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['int'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['str'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['set'], point=1, score=1),
            d.AnswerBlocks(['dict'], point=1, score=1)
            ]

question2 = d.Questions(3, ["Eat all mutable types"])

answers3 = [d.AnswerBlocks(['No'], point=1, score=1,),
            d.AnswerBlocks(['Yes'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['Maybe'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['C++', 'rules'], point=0, score=-1, life=-1),
            ]


question3 = d.Questions(1, ["Python is an compiled, interactive",
                            "object-oriented programming language."])

answers4 = [d.AnswerBlocks(['import', 'this'], point=1, score=1,),
            d.AnswerBlocks(['import', 'zen'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['import', 'that'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['import', 'import'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['import', 'export'], point=0, score=-1, life=-1),
            ]


question4 = d.Questions(1, ["What is code for printing",
                            "the Zen of Python?"])

answers5 = [d.AnswerBlocks(['a={1}', 'a[0]'], point=1, score=1,),
            d.AnswerBlocks(["1+'1'"], point=1, score=1,),
            d.AnswerBlocks(['b=[1]', 'b[0]'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['2//3'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['"2"+', '"2"'], point=0, score=-1, life=-1)
            ]

question5 = d.Questions(2,["Eat all error cases",])

answers6 = [d.AnswerBlocks(['[]'], point=1, score=1,),
            d.AnswerBlocks(['a >', 'abs(a)'], point=1, score=1,),
            d.AnswerBlocks(['0 or 1'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['"Fal', 'se"'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['[0]'], point=0, score=-1, life=-1)
            ]

question6 = d.Questions(2,["Eat all False values",])

answers7 = [d.AnswerBlocks(['6'], point=1, score=1,),
            d.AnswerBlocks(['4'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['5'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['7'], point=0, score=-1, life=-1)
            ]

question7 = d.Questions(1,["a = [1,2,3,None,(),[],]", "What is len(a)?"])

answers8 = [d.AnswerBlocks(['None'], point=1, score=1,),
            d.AnswerBlocks(['3'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['b=', '1+2'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['Error'], point=0, score=-1, life=-1)
            ]

question8 = d.Questions(1,["def a():b = 1+2",
                           "print(a())     What does it print?"])

answers9 = [d.AnswerBlocks(['inheri', 'tance'], point=1, score=1,),
            d.AnswerBlocks(['polymo', 'rphism'], point=1, score=1,),
            d.AnswerBlocks(['love'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['jus', 'tice'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['fight', 'or run'], point=0, score=-1, life=-1)
            ]

question9 = d.Questions(2,["Basic principles of OOP in Python are:",
                           "encapsulation, ..."])

answers10 = [d.AnswerBlocks(['True'], point=1, score=1,),
            d.AnswerBlocks(['all([])'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['False'], point=0, score=-1, life=-1),
            d.AnswerBlocks(['Error'], point=0, score=-1, life=-1)
            ]

question10 = d.Questions(1,["print(all([]))",
                           "What does it print?"])






questions = [question3, question4, question1, question2, question5, question6, question7, question8, question9, question10]
answers = [answers3, answers4, answers1, answers2, answers5, answers6, answers7, answers8, answers9, answers10]
q_a_list_zip = list(zip(questions, answers))



