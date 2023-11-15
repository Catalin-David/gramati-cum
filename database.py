from answer import Answer
from question import Question

def initialise_database():
    questions = []

    answer1 = Answer("7 litere, 6 sunete; 8 litere, 5 sunete; 8 litere, 8 sunete; 5 litere, 4 sunete")
    answer2 = Answer("7 litere, 5 sunete; 8 litere, 6 sunete; 8 litere, 8 sunete; 5 litere, 3 sunete")
    answer3 = Answer("7 litere, 6 sunete; 8 litere, 5 sunete; 8 litere, 6 sunete; 5 litere, 4 sunete")
    answer4 = Answer("7 litere, 6 sunete; 8 litere, 5 sunete; 8 litere, 7 sunete; 5 litere, 3 sunete")
    question = Question("Precizează seria care conține numărul corect de litere și de sunete pentru cuvintele: geamgiu, Gheorghe, nicicând, unchi:",
                        [answer1,answer2,answer3,answer4,], answer1.id)
    questions.append(question)

    answer1 = Answer("4 litere, 3 sunete; 7 litere, 7 sunete; 7 litere, 5 sunete; 7 litere, 8 sunete")
    answer2 = Answer("4 litere, 2 sunete; 7 litere, 6 sunete; 7 litere, 7 sunete; 7 litere, 7 sunete")
    answer3 = Answer("4 litere, 3 sunete; 7 litere, 7 sunete; 7 litere, 7 sunete; 7 litere, 6 sunete")
    answer4 = Answer("4 litere, 4 sunete; 7 litere, 7 sunete; 7 litere, 7 sunete; 7 litere, 8 sunete")
    question = Question("Precizează seria care conține numărul corect de litere și de sunete pentru cuvintele:chin, cianură, ketchup, xilofon:",
                        [answer1,answer2,answer3,answer4,], answer3.id)
    questions.append(question)

    answer1 = Answer("aripioară, eu, vegheau, ziceau")
    answer2 = Answer("aripioară, eu, înșeuează, pleoapă")
    answer3 = Answer("ghiceau, miau, pleoapă, scoică")
    answer4 = Answer("cearșaf, dumneaei, papuaș, toamnă")
    question = Question("Indică seria de cuvinte care conține numai triftongi:",
                        [answer1,answer2,answer3,answer4,], answer2.id)
    questions.append(question)

    answer1 = Answer("supoziție")
    answer2 = Answer("împrejurare")
    answer3 = Answer("relație")
    answer4 = Answer("context")
    question = Question("Sinonimul cuvântului conjectură este:",
                        [answer1,answer2,answer3,answer4,], answer4.id)
    questions.append(question)

    answer1 = Answer("a scrie, hotărât")
    answer2 = Answer("a publica, despotic")
    answer3 = Answer("a inspecta, imediat")
    answer4 = Answer("a revizui, numaidecât")
    question = Question("Sensurile următoarelor unități frazeologice 'a trece în revistă', 'dintr-un cuvânt' sunt, în ordine:",
                        [answer1,answer2,answer3,answer4,], answer1.id)
    questions.append(question)

    answer1 = Answer("filigram-filigran, proroc-prooroc, bleumarin-bleumaren, delicvent-delincvent")
    answer2 = Answer("filigran-filigram, proroc-prooroc, bleumaren-bleumarin, delincvent-delicvent")
    answer3 = Answer("filigran-filigram, proroc-prooroc, bleumarin-bleumaren, delincvent-delicvent")
    answer4 = Answer("filigran-filigram, prooroc-proroc, bleumarin-bleumaren, delincvent-delicvent")
    question = Question("Indică seria în care doar prima formă a cuvintelor date este corectă:",
                        [answer1,answer2,answer3,answer4,], answer1.id)
    questions.append(question)

    answer1 = Answer("șase")
    answer2 = Answer("patru")
    answer3 = Answer("trei")
    answer4 = Answer("cinci")
    question = Question("Precizează câte cuvinte formate prin procedeul compunerii sunt în seria: așadar, oricum, înflori, întruna, totuși, unsprezece",
                        [answer1,answer2,answer3,answer4,], answer1.id)
    questions.append(question)

    answer1 = Answer("brânză, lăptăreasă, lăptărie, lăptic")
    answer2 = Answer("iaurt, lactate, lăptos, lapte")
    answer3 = Answer("lăptar, lăptăreasă, lăptărie, lăptic")
    answer4 = Answer("lactație, lăptăreasă, lăptărie, lăptic")
    question = Question("Indică seria care conține numai termeni aparținând familiei lexicale a cuvântului lapte:",
                        [answer1,answer2,answer3,answer4,], answer1.id)
    questions.append(question)

    # answer1 = Answer("")
    # answer2 = Answer("")
    # answer3 = Answer("")
    # answer4 = Answer("")
    # question = Question("",
    #                     [answer1,answer2,answer3,answer4,], answer1.id)
    # questions.append(question)

    return questions