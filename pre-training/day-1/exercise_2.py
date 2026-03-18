

def grade_classifier(score):
    """
    Classify a score into a grade category.
    
    Args:
        score: The score to classify (0-100)
    
    Returns:
        A string representing the grade: 'Distinction' (90+), 'Pass' (60-89), 'Fail' (<60)
    """
    if score >= 90:
        return 'Distinction'
    elif score >= 60:
        return 'Pass'
    else:
        return 'Fail'


# Test with at least 5 values
print("Testing grade_classifier with individual scores:")
test_scores = [95, 75, 45, 88, 55, 20, 15, 99]
for score in test_scores:
    grade = grade_classifier(score)
    print(f"Score: {score} → Grade: {grade}")

# Summary
print("\n" + "="*40)
distinction_count = sum(1 for score in test_scores if grade_classifier(score) == 'Distinction')
pass_count = sum(1 for score in test_scores if grade_classifier(score) == 'Pass')
fail_count = sum(1 for score in test_scores if grade_classifier(score) == 'Fail')

print(f"Summary: {distinction_count} Distinction, {pass_count} Pass, {fail_count} Fail")

