#!/usr/bin/env python3
"""
🐛 개발자 전용 버그 핑계 생성기 🐛
당신의 버그를 정당화해줄 완벽한 핑계를 찾아드립니다!
"""

import random
from typing import List


class BugExcuseGenerator:
    """개발자의 버그 문제를 우아하게 해결해주는 마법사"""

    def __init__(self):
        self.prefixes = [
            "글쎄요, 제 컴퓨터에서는",
            "분명히 저건",
            "혹시 혹시",
            "음... 이건 사실",
            "아! 그건 뭔가",
            "제 생각엔",
            "여러분, 믿으세요",
            "스택오버플로우에 따르면",
            "어제 밤새도록",
            "뭔가 이상한데",
        ]

        self.issues = [
            "부동소수점 연산 오류라서요",
            "유니코드 문제거든요",
            "시스템 시간이 좀 꼬였어요",
            "캐시가 전혀 비워지지 않았어요",
            "Node.js 문제입니다",
            "99.999%는 제 코드가 아니라 라이브러리 버그예요",
            "제 로컬에선 작동하는데요?",
            "JavaScript의 `==` 때문이에요",
            "생일에 한 번만 터지는 버그래요",
            "인턴이 커밋한 거예요",
        ]

        self.solutions = [
            "재부팅하면 해결돼요",
            "턴테이블을 한 바퀴 돌려봤어요",
            "코드에 주석을 추가했어요",
            "더 많은 console.log를 추가했어요",
            "스택오버플로우 솔루션을 복붙했어요",
            "원래 이렇게 작동하는 거예요",
            "다음 업데이트에서 고칠게요",
            "ChatGPT한테 물었는데 모른대요",
            "그냥 프로덕션 환경에서는 작동해요",
            "버그가 아니라 미정의된 동작이에요",
        ]

    def generate_excuse(self) -> str:
        """완벽한 버그 핑계 생성"""
        prefix = random.choice(self.prefixes)
        issue = random.choice(self.issues)
        solution = random.choice(self.solutions)
        return f"{prefix} {issue}\n→ 해결책: {solution}"

    def generate_multiple(self, count: int = 5) -> str:
        """여러 개의 핑계 생성 (선택지를 드립니다)"""
        excuses = [
            f"\n【핑계 {i + 1}】\n{self.generate_excuse()}"
            for i in range(count)
        ]
        return "\n" + "=" * 50 + "".join(excuses) + "\n" + "=" * 50

    def rate_excuse(self, excuse: str) -> str:
        """핑계의 신뢰성을 평가합니다"""
        score = random.randint(1, 100)
        stars = "⭐" * (score // 20)
        return f"신뢰성: {score}% {stars}"


def main():
    """메인 프로그램"""
    generator = BugExcuseGenerator()

    print("\n" + "🎭" * 20)
    print("개발자 전용 버그 핑계 생성기에 오신 것을 환영합니다!")
    print("🎭" * 20 + "\n")

    # 단일 핑계
    print("【오늘의 추천 핑계】")
    excuse = generator.generate_excuse()
    print(excuse)
    print(f"평가: {generator.rate_excuse(excuse)}\n")

    # 여러 핑계
    print("【다양한 핑계 옵션】")
    print(generator.generate_multiple(3))

    # 최후의 수단
    print("\n【최후의 수단】")
    print("비상 핑계: '누군가 내 깃허브 계정에 접근한 것 같아요'\n")


if __name__ == "__main__":
    main()
