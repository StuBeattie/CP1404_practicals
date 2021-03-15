"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status
"""


def main():
    """Get users score and print results"""
    score = float(input("Enter score: "))
    print(results(score))


def results(score):
    """obtain results from users score"""
    if score < 0 or not score <= 100:
        return 'invalid score'
    elif score >= 90:
        return 'Excellent'
    elif score >= 50:
        return 'Passable'
    else:
        return 'Bad'


main()
