from pathlib import Path

HTML = Path(__file__).parents[1] / "index.html"


def source() -> str:
    return HTML.read_text(encoding="utf-8")


def test_resource_search_is_case_based_and_filterable():
    s = source()
    assert "selectedCaseId" in s
    assert 'id="resource-keyword"' in s
    assert 'id="resource-category"' in s
    assert 'id="resource-availability"' in s
    assert "일치 이유" in s
    assert "data-open-proposal" in s


def test_match_proposal_collects_operational_fields_and_has_preview():
    s = source()
    assert "function matchProposalForm" in s
    assert "function matchProposalPreview" in s
    assert 'id="allocation-qty"' in s
    assert 'id="delivery-date"' in s
    assert 'id="delivery-method"' in s
    assert 'id="proposal-reason"' in s
    assert 'id="lead-member"' in s
    assert 'id="support-member"' in s
    assert "data-preview-proposal" in s
    assert "data-submit-proposal" in s


def test_submitted_proposal_enters_review_queue_without_auto_approval():
    s = source()
    assert "운영 검토 대기" in s
    assert "selectedMatchId" in s
    assert "function reviewCard" in s
    assert "state.matches.filter" in s
    assert "공동 승인 0/2" in s
    assert "재고는 최종 승인 시 예약" in s


def test_new_screens_are_registered():
    s = source()
    assert "'member-match-form':matchProposalForm" in s
    assert "'member-match-preview':matchProposalPreview" in s


def test_joint_approval_requires_distinct_actors_before_inventory_reservation():
    s = source()
    assert 'id="approval-user"' in s
    assert "m.approvers.includes(actor)" in s
    assert "같은 승인자는 중복 승인할 수 없습니다" in s
    assert "m.approvalCount>=m.requiredApprovals" in s
    assert "o.qty=Math.max(0,o.qty-m.allocationQty)" in s


def test_case_cards_show_all_stages_and_current_stage():
    s = source()
    assert "function caseStage" in s
    assert "등록','검토','자원','제안','승인','전달','완료" in s
    assert "현재 단계" in s
    assert 'class="case-stage-track"' in s


def test_resource_tab_explains_donor_matching_in_plain_language():
    s = source()
    assert "['member-resources','연결','resource']" in s
    assert "등록한 케이스에 맞는 후원자의 나눔을 찾아 연결합니다" in s
    assert "연결 가능한 후원 나눔" in s
    assert "선택한 나눔으로 연결 제안" in s
    assert 'class="advanced-filter"' in s


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
