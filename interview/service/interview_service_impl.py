from typing import List, Dict

from interview.service.interview_service import InterviewService
from interview.repository.interview_repository_impl import InterviewRepositoryImpl
from interview.service.request.first_followup_question_generation_request import FirstFollowupQuestionGenerationRequest
from interview.service.request.project_followup_generation_request import ProjectFollowupGenerationRequest
from interview.service.request.project_question_generation_request import ProjectQuestionGenerationRequest
from interview.service.request.question_generation_request import FirstQuestionGenerationRequest


class InterviewServiceImpl(InterviewService):
    def __init__(self):
        self.interviewRepository = InterviewRepositoryImpl()

    # 인터뷰 첫질문 생성 + 첫질문의 꼬리질문
    def generateInterviewQuestions(self, request: FirstQuestionGenerationRequest) -> dict:
        interviewId = request.interviewId
        topic = request.topic
        experienceLevel = request.experienceLevel
        userToken = request.userToken

        print(f"💡 [service] Requesting question generation for interviewId={interviewId}")

        questions = self.interviewRepository.generateQuestions(
            interviewId, topic, experienceLevel, userToken
        )

        return {
            "interviewId": interviewId,
            "questions": questions
        }

    def generateFirstFollowupQuestions(self, request: FirstFollowupQuestionGenerationRequest) -> dict:
        interviewId = request.interviewId
        topic = request.topic
        experienceLevel = request.experienceLevel
        academicBackground = request.academicBackground
        questionId = request.questionId
        answerText = request.answerText
        userToken = request.userToken

        print(f"💡 [service] Requesting first follow-up questions for interviewId={interviewId}")

        questions = self.interviewRepository.generateFirstFollowup(
            interviewId, topic, experienceLevel, academicBackground,questionId, answerText, userToken
        )

        return {
            "interviewId": interviewId,
            "questions": questions
        }

    # 프로젝트 첫질문 생성
    def generateProjectQuestion(self, request: ProjectQuestionGenerationRequest) -> dict:
        interviewId = request.interviewId
        projectExperience = request.projectExperience
        userToken = request.userToken

        print(f"💡 [service] Requesting question generation for interviewId={interviewId}")

        questions = self.interviewRepository.generateProjectQuestion(
            interviewId, projectExperience, userToken
        )

        return {
            "interviewId": interviewId,
            "questions": questions
        }


    def generateProjectFollowupQuestion(self, request: ProjectFollowupGenerationRequest) -> dict:
        interviewId = request.interviewId
        topic: request.topic
        techStack: request.techStack
        projectExperience = request.experienceLevel
        questionId = request.questionId
        answerText = request.answerText
        userToken = request.userToken
        print(f"💡 [service] Requesting follow-up question for interviewId={interviewId}, questionId={questionId}")

        followup_question = self.interviewRepository.generateProjectFollowupQuestion(
            interviewId, topic, techStack, projectExperience, questionId, answerText, userToken
        )

        return {
            "interviewId": interviewId,
            "questions": followup_question
        }


    def end_interview(self,
        sessionId: str,
        context: Dict[str, str],
        questions: List[str],
        answers: List[str]
    ) -> Dict:
        return self.interviewRepository.end_interview(sessionId, context, questions, answers)