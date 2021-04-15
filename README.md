# Automated-Q-A-System

## 1.1 Project Introduction
The Indian education landscape has been undergoing rapid changes for the past 10 years owing to
the advancement of web-based learning services, specifically, eLearning platforms.
Most online education institutes today treat all students in the same class/batch/cohort (referred to as
“group” hereinafter) the same. Institutional uniformity works quite well for machines but humans are
made up of different and often contradictory components!
We believe that the model of allowing all students to learn at the same pace with the same level of
interest is quite detrimental to the quality of education. This model is testing the capabilities of
students by forcing them to work together in groups at the same pace, regardless of each individual's
ability and the interests of the work.
The reality could not be farther from the truth. The reason we see a wide variation in the group
performance is owing to this thought process.
In a system based on Competency Based Learning (referred to as “CBL” going forward), the group is
accepted as a set of diverse individuals who may come with some common traits but also recognizes
their different educational backgrounds, life & work experiences and learning styles.
Competency-based learning is an approach to education that focuses on the student’s demonstration
of desired learning outcomes as central to the learning process. A key characteristic of
competency-based learning is its focus on mastery. In other learning models, students are exposed to
content–whether skills or concepts–over time, and success is measured on a summative basis. In a
competency-based learning system, students are not allowed to continue until they have
demonstrated mastery of the identified competencies (i.e., the desired learning outcomes to be
demonstrated).
It is quite common to see students get stuck, fall behind, give up & in extreme cases – drop out of the
program in the traditional model of education. A standard experience for a student in this model is
“failing” and then having to repeat the class/subject/year till they are able to achieve a passing grade.
This causes the student to lose interest in addition to social embarrassment. The result is a student
who is now trying to “pass” by rote memorization and doing the bare minimum for the passing.
While assessments based on rubrics are a cornerstone for the CBL system as well – they serve the
purpose of reinforcing the concepts, and to show the student & the instructor(s) how well understood
are each of the concepts and their application; rather than making just a judgment of passing and
failing.
In this light, to be able to cater to a large pool of students to enable seamless learning, we envision an
automated doubt resolution system. In the era of advancing AI technology, most of the doubts can be
resolved via deep learning techniques. The AI system in place can understand the context of the
question and can provide relevant answers to the questions.

## 1.2 Problem Statement
We will solve the above-mentioned challenge by applying deep learning algorithms to textual data.
The solution to this problem can be obtained through Extractive Question Answering wherein we can
extract an answer from a text given the question.

### 1.2.1 Topic Modelling
This is a theme extraction task on a collection of Data Science specific documents which can be done
via Latent Dirichlet Allocation (LDA). The topic model should identify the important themes of a
document and list down the top-N constituent words of the themes/topics.

### 1.2.2 Extractive Question Answering
Extractive Question Answering is the task of extracting an answer from a text given a question. The
text would essentially be the group of documents that have the highest concentration of the topic
closest to the asked question.
