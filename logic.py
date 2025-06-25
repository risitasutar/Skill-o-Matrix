# logic.py

def evaluate_quiz(quiz_section, answers, current_quiz):
    questions = current_quiz[quiz_section]["questions"]
    score = 0
    feedback = []

    for i, q in enumerate(questions):
        correct = q["answer"]
        given = answers[i]
        is_correct = given == correct
        score += int(is_correct)
        feedback.append({
            "question": q["question"],
            "your_answer": given,
            "correct_answer": correct,
            "is_correct": is_correct
        })

    result = {
        "total_questions": len(questions),
        "score": score,
        "percentage": (score / len(questions)) * 100,
        "feedback": feedback
    }
    return result

quiz = {
    "Data Science": {
        "questions": [
            # 30 sample questions covering Python, Excel, and ML
            {"question": "What is the primary library for numerical computing in Python?", "options": ["A. pandas", "B. numpy", "C. matplotlib", "D. scipy"], "answer": "B"},
            {"question": "Which Excel function calculates the median?", "options": ["A. AVERAGE()", "B. MEDIAN()", "C. MODE()", "D. MID()"], "answer": "B"},
            {"question": "Which ML algorithm is used for classification?", "options": ["A. Linear Regression", "B. Decision Tree", "C. KMeans", "D. PCA"], "answer": "B"},
            {"question": "Which function is used to get top rows in pandas?", "options": ["A. head()", "B. top()", "C. first()", "D. sample()"], "answer": "A"},
            {"question": "Which chart is best to visualize categories in Excel?", "options": ["A. Line chart", "B. Pie chart", "C. Scatter plot", "D. Histogram"], "answer": "B"},
            {"question": "Which metric evaluates classification accuracy?", "options": ["A. RMSE", "B. MSE", "C. Accuracy", "D. R2"], "answer": "C"},
            {"question": "Which method removes duplicates in pandas?", "options": ["A. dropna()", "B. remove_duplicates()", "C. drop_duplicates()", "D. filter_duplicates()"], "answer": "C"},
            {"question": "Which function calculates correlation in pandas?", "options": ["A. correlate()", "B. corr()", "C. correlation()", "D. coef()"], "answer": "B"},
            {"question": "Which Excel feature allows filtering data?", "options": ["A. Sort", "B. Chart", "C. Filter", "D. Formula"], "answer": "C"},
            {"question": "Which Python package is used for data visualization?", "options": ["A. seaborn", "B. sklearn", "C. flask", "D. keras"], "answer": "A"},
            {"question": "Which method is used to split data in scikit-learn?", "options": ["A. split_data()", "B. data_split()", "C. train_test_split()", "D. divide()"], "answer": "C"},
            {"question": "Which Excel function rounds numbers?", "options": ["A. FLOOR()", "B. ROUND()", "C. ROUNDUP()", "D. ROUNDOWN()"], "answer": "B"},
            {"question": "Which evaluation metric is for regression?", "options": ["A. Confusion Matrix", "B. Accuracy", "C. MAE", "D. F1 Score"], "answer": "C"},
            {"question": "What does df.shape return in pandas?", "options": ["A. Columns only", "B. Shape of cells", "C. Rows & columns", "D. Column names"], "answer": "C"},
            {"question": "Which Python IDE is preferred for Data Science?", "options": ["A. VS Code", "B. Jupyter", "C. Atom", "D. IDLE"], "answer": "B"},
            {"question": "Which Excel feature performs what-if analysis?", "options": ["A. Filter", "B. Goal Seek", "C. VLOOKUP", "D. Index Match"], "answer": "B"},
            {"question": "Which ML model handles non-linearity well?", "options": ["A. Linear Regression", "B. Logistic Regression", "C. Decision Tree", "D. Naive Bayes"], "answer": "C"},
            {"question": "Which function shows null values in pandas?", "options": ["A. is_null()", "B. isna()", "C. null()", "D. checkna()"], "answer": "B"},
            {"question": "Which method normalizes data?", "options": ["A. MinMaxScaler", "B. StandardScaler", "C. RobustScaler", "D. All of these"], "answer": "D"},
            {"question": "What is used to reduce overfitting in ML?", "options": ["A. Regularization", "B. More layers", "C. Larger test set", "D. Cross entropy"], "answer": "A"},
            {"question": "Which function displays histogram in matplotlib?", "options": ["A. plot()", "B. hist()", "C. bar()", "D. box()"], "answer": "B"},
            {"question": "Which pandas function resets index?", "options": ["A. index_reset()", "B. reset_index()", "C. drop_index()", "D. reindex()"], "answer": "B"},
            {"question": "Which ML library contains pipelines?", "options": ["A. sklearn", "B. tensorflow", "C. keras", "D. pandas"], "answer": "A"},
            {"question": "Which file format is best for structured data?", "options": ["A. .txt", "B. .csv", "C. .html", "D. .log"], "answer": "B"},
            {"question": "What is overfitting?", "options": ["A. Low error", "B. Model fits noise", "C. Model too simple", "D. High bias"], "answer": "B"},
            {"question": "Which function combines columns in pandas?", "options": ["A. concat()", "B. combine()", "C. add()", "D. merge()"], "answer": "A"},
            {"question": "Which Python type represents table-like data?", "options": ["A. Series", "B. List", "C. DataFrame", "D. Dict"], "answer": "C"},
            {"question": "Which chart best shows trend?", "options": ["A. Pie", "B. Line", "C. Bar", "D. Histogram"], "answer": "B"},
            {"question": "Which Excel formula joins text?", "options": ["A. TEXT()", "B. CONCATENATE()", "C. MERGE()", "D. JOIN()"], "answer": "B"},
            {"question": "What does feature engineering mean?", "options": ["A. Adding noise", "B. Cleaning data", "C. Creating input features", "D. Deleting rows"], "answer": "C"}
        ]
    },

    "Software Fundamentals": {
        "questions": [
            {"question": "Which of the following is a valid C++ identifier?", "options": ["A. 123var", "B. my_var", "C. my-var", "D. @count"], "answer": "B"},
            {"question": "What does the 'sizeof' operator do in C++?", "options": ["A. Returns memory size", "B. Converts types", "C. Finds size of string", "D. None"], "answer": "A"},
            {"question": "Which loop checks condition at the end?", "options": ["A. for", "B. while", "C. do-while", "D. until"], "answer": "C"},
            {"question": "Which of these is not a data type in C++?", "options": ["A. int", "B. float", "C. string", "D. real"], "answer": "D"},
            {"question": "What is the default return type of a function in C++?", "options": ["A. void", "B. int", "C. double", "D. float"], "answer": "B"},
            {"question": "Which keyword is used for inheritance?", "options": ["A. extends", "B. implements", "C. public", "D. inherit"], "answer": "C"},
            {"question": "Which is not a logical operator in C++?", "options": ["A. &&", "B. ||", "C. !", "D. %%"], "answer": "D"},
            {"question": "Which header is needed for string operations?", "options": ["A. iostream", "B. stdlib.h", "C. string", "D. string.h"], "answer": "C"},
            {"question": "Which operator is used for dereferencing?", "options": ["A. *", "B. &", "C. ->", "D. ::"], "answer": "A"},
            {"question": "Which concept allows reusability in OOP?", "options": ["A. Inheritance", "B. Encapsulation", "C. Abstraction", "D. Polymorphism"], "answer": "A"},
            {"question": "Which is the correct way to declare a pointer?", "options": ["A. int *p;", "B. int p*;", "C. *int p;", "D. p int*;"], "answer": "A"},
            {"question": "What is the output type of cin.get()?", "options": ["A. string", "B. char", "C. int", "D. bool"], "answer": "B"},
            {"question": "Which file extension is correct for a C++ header?", "options": ["A. .c", "B. .hpp", "C. .h", "D. .hh"], "answer": "C"},
            {"question": "What is used to prevent multiple inclusions of header files?", "options": ["A. #pragma once", "B. #ifndef", "C. #define", "D. All of the above"], "answer": "D"},
            {"question": "Which is a valid function declaration?", "options": ["A. func();", "B. void func()", "C. void func(){}", "D. func{}"], "answer": "C"},
            {"question": "Which STL container allows key-value pairs?", "options": ["A. vector", "B. list", "C. map", "D. queue"], "answer": "C"},
            {"question": "Which container allows duplicate keys?", "options": ["A. set", "B. map", "C. multimap", "D. unordered_map"], "answer": "C"},
            {"question": "Which function adds an element to the end of vector?", "options": ["A. push_front()", "B. insert()", "C. append()", "D. push_back()"], "answer": "D"},
            {"question": "Which is used to handle errors in C++?", "options": ["A. if-else", "B. try-catch", "C. switch", "D. throw-catch"], "answer": "B"},
            {"question": "What is the output of: sizeof(char)?", "options": ["A. 2", "B. 4", "C. 1", "D. 8"], "answer": "C"}
        ,
            # 30 sample questions for C++, logic and fundamentals
            {"question": "Which language uses 'std::cout'?", "options": ["A. Java", "B. C++", "C. Python", "D. C#"], "answer": "B"},
            {"question": "What is the extension of C++ files?", "options": ["A. .c", "B. .java", "C. .cpp", "D. .py"], "answer": "C"},
            {"question": "What is function overloading?", "options": ["A. Functions with same name & diff params", "B. Two classes", "C. Using two functions", "D. Nested function"], "answer": "A"},
            {"question": "Which keyword allocates dynamic memory?", "options": ["A. malloc", "B. new", "C. alloc", "D. create"], "answer": "B"},
            {"question": "Which is a loop structure?", "options": ["A. if", "B. for", "C. class", "D. switch"], "answer": "B"},
            {"question": "Which keyword is used to define a class?", "options": ["A. def", "B. struct", "C. class", "D. object"], "answer": "C"},
            {"question": "Which header file includes 'cout'?", "options": ["A. iostream", "B. stdio.h", "C. conio.h", "D. math.h"], "answer": "A"},
            {"question": "Which operator is used for address?", "options": ["A. *", "B. &", "C. @", "D. ^"], "answer": "B"},
            {"question": "Which symbol comments a line in C++?", "options": ["A. //", "B. #", "C. **", "D. ;;"], "answer": "A"},
            {"question": "What is a pointer?", "options": ["A. Variable", "B. Object", "C. Stores address", "D. Type of loop"], "answer": "C"}
            # You can add 20 more questions here similarly for full coverage.
        ]
    },
    "Core: Civil Engineering": {
        "questions": [
            {"question": "Which material is most commonly used in concrete?",
             "options": ["A. Steel", "B. Cement", "C. Wood", "D. Asphalt"], "answer": "B"},
            {"question": "Which test checks concrete compressive strength?",
             "options": ["A. Slump test", "B. CBR test", "C. Compression test", "D. Flexural test"], "answer": "C"},
            {"question": "Which structure resists bending moments?",
             "options": ["A. Column", "B. Beam", "C. Slab", "D. Footing"], "answer": "B"},
            {"question": "What does RCC stand for?",
             "options": ["A. Reinforced Cement Concrete", "B. Ready Concrete Cast", "C. Rough Cast Concrete",
                         "D. Reactive Composite Cement"], "answer": "A"},
            {"question": "Which surveying tool measures angles?",
             "options": ["A. Theodolite", "B. Level", "C. Compass", "D. Tapes"], "answer": "A"},
            {"question": "What is the unit of stress?", "options": ["A. N", "B. N/m", "C. N/m²", "D. m/s²"],
             "answer": "C"},
            {"question": "Which foundation is used for tall buildings?",
             "options": ["A. Shallow", "B. Strip", "C. Raft", "D. Pile"], "answer": "D"},
            {"question": "Which load acts vertically downwards?",
             "options": ["A. Dead load", "B. Wind load", "C. Seismic load", "D. Live load"], "answer": "A"},
            {"question": "Slump test is used for:",
             "options": ["A. Workability", "B. Strength", "C. Water content", "D. Setting time"], "answer": "A"},
            {"question": "Which code is used for general construction?",
             "options": ["A. IS 456", "B. IS 800", "C. IS 10262", "D. IS 1893"], "answer": "A"}
        ]
    },

    "Core: Chemical Engineering": {
        "questions": [
            {"question": "What does a catalyst do?",
             "options": ["A. Slows reaction", "B. Increases temperature", "C. Speeds reaction", "D. Absorbs heat"],
             "answer": "C"},
            {"question": "Which law relates pressure and volume?",
             "options": ["A. Boyle’s Law", "B. Charles’ Law", "C. Avogadro’s Law", "D. Newton’s Law"], "answer": "A"},
            {"question": "Which reactor is best for batch operations?",
             "options": ["A. CSTR", "B. PFR", "C. Batch reactor", "D. Tubular reactor"], "answer": "C"},
            {"question": "What is the unit of viscosity?", "options": ["A. Pa", "B. N/m²", "C. Pa·s", "D. m/s²"],
             "answer": "C"},
            {"question": "Which equipment separates mixtures?",
             "options": ["A. Reactor", "B. Distillation column", "C. Heat exchanger", "D. Evaporator"], "answer": "B"},
            {"question": "Which process removes heat?",
             "options": ["A. Exothermic", "B. Endothermic", "C. Distillation", "D. Cooling"], "answer": "D"},
            {"question": "What is a fluid with no viscosity?",
             "options": ["A. Real fluid", "B. Ideal fluid", "C. Newtonian", "D. Gas"], "answer": "B"},
            {"question": "pH 7 represents:", "options": ["A. Acidic", "B. Basic", "C. Neutral", "D. Alkaline"],
             "answer": "C"},
            {"question": "Which is a unit of concentration?", "options": ["A. Pa", "B. mol/L", "C. kg", "D. m/s"],
             "answer": "B"},
            {"question": "The gas constant (R) has units:", "options": ["A. J/mol·K", "B. N/m", "C. Pa", "D. W/K"],
             "answer": "A"}
        ]
    },
    "Core: Ceramic Engineering": {
        "questions": [
            {"question": "Which material is commonly used in ceramics?",
             "options": ["A. Silica", "B. Iron", "C. Aluminum", "D. Copper"], "answer": "A"},
            {"question": "Which process is used to shape ceramic materials?",
             "options": ["A. Sintering", "B. Forging", "C. Rolling", "D. Welding"], "answer": "A"},
            {"question": "Ceramics are generally:",
             "options": ["A. Ductile", "B. Brittle", "C. Malleable", "D. Flexible"], "answer": "B"},
            {"question": "What is used to fuse ceramic particles?",
             "options": ["A. Flux", "B. Clay", "C. Alumina", "D. Cement"], "answer": "A"},
            {"question": "Which test measures ceramic hardness?",
             "options": ["A. Brinell", "B. Mohs", "C. Charpy", "D. Rockwell"], "answer": "B"},
            {"question": "Which of these is a glass-ceramic?",
             "options": ["A. Pyrex", "B. Alumina", "C. Kaolin", "D. Spinel"], "answer": "A"},
            {"question": "Ceramic materials resist:",
             "options": ["A. Corrosion", "B. Heat", "C. Electrical conductivity", "D. Plastic deformation"],
             "answer": "B"},
            {"question": "What is the raw material for porcelain?",
             "options": ["A. Kaolin", "B. Sand", "C. Talc", "D. Feldspar"], "answer": "A"},
            {"question": "Which property makes ceramics good insulators?",
             "options": ["A. High porosity", "B. Ionic bonding", "C. Covalent bonding", "D. Free electrons"],
             "answer": "B"},
            {"question": "Which technique creates ceramic coatings?",
             "options": ["A. Plasma spraying", "B. Welding", "C. Dip coating", "D. Galvanizing"], "answer": "A"}
        ]
    },

    "Core: Computer Science Engineering": {
        "questions": [
            {"question": "Which data structure uses FIFO?", "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
             "answer": "B"},
            {"question": "Which language is primarily used for system programming?",
             "options": ["A. Python", "B. Java", "C. C", "D. HTML"], "answer": "C"},
            {"question": "What does CPU stand for?",
             "options": ["A. Central Processing Unit", "B. Computer Processing Unit", "C. Core Processing Unit",
                         "D. Compute Power Unit"], "answer": "A"},
            {"question": "Which sort is fastest in average case?",
             "options": ["A. Bubble", "B. Merge", "C. Quick", "D. Insertion"], "answer": "C"},
            {"question": "Which protocol is used for web?", "options": ["A. FTP", "B. HTTP", "C. SSH", "D. SMTP"],
             "answer": "B"},
            {"question": "What is the binary of 5?", "options": ["A. 1000", "B. 0101", "C. 1100", "D. 0011"],
             "answer": "B"},
            {"question": "What is a class in OOP?",
             "options": ["A. Object", "B. Blueprint", "C. Variable", "D. Method"], "answer": "B"},
            {"question": "Which of these is a NoSQL database?",
             "options": ["A. MySQL", "B. PostgreSQL", "C. MongoDB", "D. SQLite"], "answer": "C"},
            {"question": "Which layer handles routing in OSI?",
             "options": ["A. Transport", "B. Session", "C. Network", "D. Data Link"], "answer": "C"},
            {"question": "What is the time complexity of binary search?",
             "options": ["A. O(n)", "B. O(log n)", "C. O(n log n)", "D. O(1)"], "answer": "B"}
        ]
    },
    "Core: Biotechnology Engineering": {
        "questions": [
            {"question": "Which molecule stores genetic information?",
             "options": ["A. DNA", "B. RNA", "C. Protein", "D. Lipid"], "answer": "A"},
            {"question": "Which technique is used for DNA amplification?",
             "options": ["A. PCR", "B. ELISA", "C. Western Blot", "D. Spectroscopy"], "answer": "A"},
            {"question": "Enzymes act as:", "options": ["A. Substrates", "B. Catalysts", "C. Inhibitors", "D. Buffers"],
             "answer": "B"},
            {"question": "What is the building block of proteins?",
             "options": ["A. Nucleotides", "B. Amino acids", "C. Fatty acids", "D. Sugars"], "answer": "B"},
            {"question": "Which organelle is responsible for energy production?",
             "options": ["A. Ribosome", "B. Golgi", "C. Mitochondria", "D. Nucleus"], "answer": "C"},
            {"question": "Which vector is commonly used in genetic engineering?",
             "options": ["A. Virus", "B. Plasmid", "C. Chromosome", "D. Ribosome"], "answer": "B"},
            {"question": "Which process produces ethanol from glucose?",
             "options": ["A. Photosynthesis", "B. Fermentation", "C. Respiration", "D. Glycolysis"], "answer": "B"},
            {"question": "Which method is used to separate proteins?",
             "options": ["A. Electrophoresis", "B. PCR", "C. Spectrophotometry", "D. Dialysis"], "answer": "A"},
            {"question": "The study of microorganisms is called:",
             "options": ["A. Virology", "B. Pathology", "C. Microbiology", "D. Immunology"], "answer": "C"},
            {"question": "CRISPR is used for:",
             "options": ["A. Gene Editing", "B. Cloning", "C. Protein folding", "D. Drug delivery"], "answer": "A"}
        ]
    },

    "Core: Biomedical Engineering": {
        "questions": [
            {"question": "Which imaging technique uses X-rays?",
             "options": ["A. MRI", "B. CT Scan", "C. Ultrasound", "D. ECG"], "answer": "B"},
            {"question": "What does ECG measure?",
             "options": ["A. Blood pressure", "B. Brain activity", "C. Heart activity", "D. Lung function"],
             "answer": "C"},
            {"question": "Which sensor measures pressure?",
             "options": ["A. Thermistor", "B. Accelerometer", "C. Barometer", "D. Strain gauge"], "answer": "D"},
            {"question": "Which device is used to monitor brain activity?",
             "options": ["A. ECG", "B. EEG", "C. EMG", "D. CT"], "answer": "B"},
            {"question": "MRI stands for:",
             "options": ["A. Magnetic Radio Imaging", "B. Magnetic Resonance Imaging", "C. Magnetic Recording Image",
                         "D. Mechanical Resonance Imaging"], "answer": "B"},
            {"question": "What unit is used to measure blood pressure?",
             "options": ["A. mmHg", "B. Pa", "C. bar", "D. psi"], "answer": "A"},
            {"question": "What material is commonly used in bone implants?",
             "options": ["A. Copper", "B. Titanium", "C. Aluminum", "D. Iron"], "answer": "B"},
            {"question": "Which organ is transplanted most frequently?",
             "options": ["A. Heart", "B. Kidney", "C. Liver", "D. Lung"], "answer": "B"},
            {"question": "Which signal type is used in bioelectronics?",
             "options": ["A. Digital", "B. Analog", "C. Electromagnetic", "D. Audio"], "answer": "B"},
            {"question": "What is the function of a pacemaker?",
             "options": ["A. Replace heart", "B. Pump blood", "C. Regulate heartbeat", "D. Filter blood"],
             "answer": "C"}
        ]
    },
    "Core: Electrical Engineering": {
        "questions": [
            {"question": "What is the SI unit of electric current?",
             "options": ["A. Volt", "B. Watt", "C. Ampere", "D. Ohm"], "answer": "C"},
            {"question": "What is Ohm's Law?", "options": ["A. V = IR", "B. P = IV", "C. V = P/I", "D. R = VI"],
             "answer": "A"},
            {"question": "Which instrument measures current?",
             "options": ["A. Voltmeter", "B. Ammeter", "C. Wattmeter", "D. Multimeter"], "answer": "B"},
            {"question": "Which device stores charge?",
             "options": ["A. Inductor", "B. Capacitor", "C. Resistor", "D. Diode"], "answer": "B"},
            {"question": "AC stands for:",
             "options": ["A. Alternate Charge", "B. Alternating Current", "C. Active Current", "D. Average Current"],
             "answer": "B"},
            {"question": "Which material is a good conductor?",
             "options": ["A. Rubber", "B. Wood", "C. Copper", "D. Plastic"], "answer": "C"},
            {"question": "What converts AC to DC?",
             "options": ["A. Inverter", "B. Amplifier", "C. Rectifier", "D. Oscillator"], "answer": "C"},
            {"question": "Which is a passive component?",
             "options": ["A. Transistor", "B. IC", "C. Resistor", "D. Relay"], "answer": "C"},
            {"question": "Power is measured in:", "options": ["A. Ampere", "B. Ohm", "C. Volt", "D. Watt"],
             "answer": "D"},
            {"question": "What is used to protect circuits from overcurrent?",
             "options": ["A. Capacitor", "B. Diode", "C. Transformer", "D. Fuse"], "answer": "D"}
        ]
    },

    "Core: Food Processing Engineering": {
        "questions": [
            {"question": "Pasteurization is used to:",
             "options": ["A. Freeze food", "B. Kill microbes", "C. Ferment food", "D. Add flavor"], "answer": "B"},
            {"question": "Which vitamin is heat-sensitive?", "options": ["A. A", "B. C", "C. D", "D. E"],
             "answer": "B"},
            {"question": "Which method removes water content?",
             "options": ["A. Sterilization", "B. Drying", "C. Freezing", "D. Cooking"], "answer": "B"},
            {"question": "Aseptic packaging is done to:",
             "options": ["A. Color food", "B. Increase volume", "C. Preserve sterile condition", "D. Pasteurize again"],
             "answer": "C"},
            {"question": "Which additive prevents spoilage?",
             "options": ["A. Preservative", "B. Antioxidant", "C. Binder", "D. Stabilizer"], "answer": "A"},
            {"question": "HTST means:",
             "options": ["A. High Temp Short Time", "B. Heat Transfer Super Treatment", "C. High Toxin Safety Test",
                         "D. Homogenized Thermal Steam Transfer"], "answer": "A"},
            {"question": "Which pH value is acidic?", "options": ["A. 1", "B. 7", "C. 10", "D. 14"], "answer": "A"},
            {"question": "Freezing slows down:",
             "options": ["A. Cooking", "B. Microbial activity", "C. Oxidation", "D. Packaging"], "answer": "B"},
            {"question": "Which enzyme breaks down starch?",
             "options": ["A. Protease", "B. Lipase", "C. Amylase", "D. Cellulase"], "answer": "C"},
            {"question": "FSSAI is responsible for:",
             "options": ["A. Food transport", "B. Food safety", "C. Food pricing", "D. Food exports"], "answer": "B"}
        ]
    },

    "Core: Industrial Design": {
        "questions": [
            {"question": "What is a prototype?",
             "options": ["A. Final product", "B. Concept", "C. Preliminary model", "D. Software"], "answer": "C"},
            {"question": "Which software is used for 3D modeling?",
             "options": ["A. Photoshop", "B. AutoCAD", "C. Excel", "D. Word"], "answer": "B"},
            {"question": "User-centered design focuses on:",
             "options": ["A. Aesthetics", "B. Function", "C. User needs", "D. Trends"], "answer": "C"},
            {"question": "Which tool is used for brainstorming?",
             "options": ["A. Pie chart", "B. Gantt chart", "C. Mind map", "D. Blueprint"], "answer": "C"},
            {"question": "What is ergonomics?",
             "options": ["A. Energy efficiency", "B. Space planning", "C. Human comfort & usability",
                         "D. Design color"], "answer": "C"},
            {"question": "CAD stands for:",
             "options": ["A. Computer-Aided Design", "B. Control Analysis Design", "C. Creative and Digital",
                         "D. Component Architecture Design"], "answer": "A"},
            {"question": "Rapid prototyping means:",
             "options": ["A. Fast sketching", "B. Quick production", "C. Early testing", "D. All of these"],
             "answer": "D"},
            {"question": "Which principle focuses on less clutter?",
             "options": ["A. Balance", "B. Simplicity", "C. Contrast", "D. Hierarchy"], "answer": "B"},
            {"question": "Which tool evaluates design usability?",
             "options": ["A. Survey", "B. Wireframe", "C. User testing", "D. Mood board"], "answer": "C"},
            {"question": "Design thinking starts with:",
             "options": ["A. Ideate", "B. Test", "C. Empathize", "D. Prototype"], "answer": "C"}
        ]
    },
    "Core: Mechanical Engineering": {
        "questions": [
            {"question": "Which law is related to motion?",
             "options": ["A. Newton's Law", "B. Boyle's Law", "C. Bernoulli's Principle", "D. Pascal's Law"],
             "answer": "A"},
            {"question": "Thermodynamics is the study of:",
             "options": ["A. Fluids", "B. Energy & heat", "C. Machines", "D. Stress"], "answer": "B"},
            {"question": "Stress is defined as:",
             "options": ["A. Force/Area", "B. Mass*Acceleration", "C. Pressure*Volume", "D. Force*Distance"],
             "answer": "A"},
            {"question": "Which cycle is used in IC engines?",
             "options": ["A. Otto cycle", "B. Diesel cycle", "C. Carnot cycle", "D. Rankine cycle"], "answer": "A"},
            {"question": "Lathe machine is used for:",
             "options": ["A. Cutting", "B. Casting", "C. Forging", "D. Drilling"], "answer": "A"},
            {"question": "Pascal's Law deals with:",
             "options": ["A. Fluid pressure", "B. Heat transfer", "C. Thermodynamics", "D. Electricity"],
             "answer": "A"},
            {"question": "Which material is hardest?", "options": ["A. Steel", "B. Diamond", "C. Iron", "D. Graphite"],
             "answer": "B"},
            {"question": "Welding joins metal by:", "options": ["A. Glue", "B. Rivets", "C. Heat", "D. Nails"],
             "answer": "C"},
            {"question": "The unit of power is:", "options": ["A. Watt", "B. Joule", "C. Newton", "D. Ampere"],
             "answer": "A"},
            {"question": "Which fluid property resists flow?",
             "options": ["A. Density", "B. Viscosity", "C. Pressure", "D. Velocity"], "answer": "B"}
        ]
    },

    "Core: Metallurgical and Materials Engineering": {
        "questions": [
            {"question": "Which test measures hardness?", "options": ["A. Charpy", "B. Brinell", "C. Izod", "D. Creep"],
             "answer": "B"},
            {"question": "What is alloying?", "options": ["A. Melting", "B. Mixing metals", "C. Casting", "D. Forging"],
             "answer": "B"},
            {"question": "Which element is added to steel to make stainless?",
             "options": ["A. Copper", "B. Chromium", "C. Zinc", "D. Nickel"], "answer": "B"},
            {"question": "Which is a non-ferrous metal?",
             "options": ["A. Iron", "B. Steel", "C. Copper", "D. Cast iron"], "answer": "C"},
            {"question": "Tempering is done to:",
             "options": ["A. Harden metal", "B. Soften metal", "C. Remove impurities", "D. Add ductility"],
             "answer": "D"},
            {"question": "Which process purifies aluminum?",
             "options": ["A. Smelting", "B. Electrolysis", "C. Roasting", "D. Bessemer"], "answer": "B"},
            {"question": "What is a phase diagram?",
             "options": ["A. Blueprint", "B. Thermal curve", "C. Equilibrium chart", "D. Structural map"],
             "answer": "C"},
            {"question": "Which property is tested by fatigue test?",
             "options": ["A. Strength", "B. Flexibility", "C. Endurance", "D. Elasticity"], "answer": "C"},
            {"question": "Which method tests impact strength?",
             "options": ["A. Brinell", "B. Vickers", "C. Izod", "D. Rockwell"], "answer": "C"},
            {"question": "Heat treatment includes:",
             "options": ["A. Heating only", "B. Cooling only", "C. Heating and cooling", "D. Smelting"], "answer": "C"}
        ]
    },

    "Core: Mining Engineering": {
        "questions": [
            {"question": "Which is a surface mining method?",
             "options": ["A. Shaft mining", "B. Strip mining", "C. Room and Pillar", "D. Drift mining"], "answer": "B"},
            {"question": "Overburden refers to:",
             "options": ["A. Ore", "B. Waste rock", "C. Valuable minerals", "D. Soil"], "answer": "B"},
            {"question": "Which explosive is used in blasting?", "options": ["A. TNT", "B. RDX", "C. ANFO", "D. C-4"],
             "answer": "C"},
            {"question": "Which law ensures mine safety in India?",
             "options": ["A. Mines Act 1952", "B. Factory Act 1948", "C. Labor Law 1961", "D. Coal Act"],
             "answer": "A"},
            {"question": "What is beneficiation?",
             "options": ["A. Drilling", "B. Blasting", "C. Ore concentration", "D. Surveying"], "answer": "C"},
            {"question": "Which equipment hauls ore?",
             "options": ["A. Loader", "B. Conveyor", "C. Dumper", "D. Excavator"], "answer": "C"},
            {"question": "Subsurface mining method?",
             "options": ["A. Open pit", "B. Strip", "C. Longwall", "D. Hydraulic"], "answer": "C"},
            {"question": "Which mineral is used in steel making?",
             "options": ["A. Bauxite", "B. Iron ore", "C. Limestone", "D. Copper"], "answer": "B"},
            {"question": "Mine ventilation removes:", "options": ["A. Gas", "B. Dust", "C. Heat", "D. All of these"],
             "answer": "D"},
            {"question": "Grade of ore means:",
             "options": ["A. Depth", "B. Thickness", "C. Concentration of metal", "D. Hardness"], "answer": "C"}
        ]
    },

}
