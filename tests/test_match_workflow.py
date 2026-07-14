from pathlib import Path

HTML = Path(__file__).parents[1] / "index.html"


def source() -> str:
    return HTML.read_text(encoding="utf-8")


def test_resource_catalog_is_newest_first_and_filterable():
    s = source()
    assert "function availableOffers" in s
    assert 'id="resource-keyword"' in s
    assert 'id="resource-category"' in s
    assert 'id="resource-availability"' in s
    assert "localeCompare" in s
    assert "data-resource-category" in s
    assert "data-open-case-picker" in s


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
    assert "후원 나눔 먼저 선택" in s
    assert "연결할 미매칭 케이스를 고릅니다" in s
    assert "후원 물품·서비스" in s
    assert "선택한 나눔에 케이스 연결" in s
    assert 'class="advanced-filter"' in s


def test_case_registration_recommends_similar_offers_before_match_request():
    s = source()
    assert 'name="category"' in s
    assert 'name="requiredQty"' in s
    assert 'name="unit"' in s
    assert "function caseRecommendations" in s
    assert "유사한 후원 나눔" in s
    assert "data-use-recommendation" in s
    assert "'case-recommendations':caseRecommendations" in s


def test_connection_tab_lists_newest_offers_before_unmatched_case_picker():
    s = source()
    assert "최신 등록순" in s
    assert "data-resource-category" in s
    assert "function matchableCases" in s
    assert "function memberSelectCase" in s
    assert "data-open-case-picker" in s
    assert "data-select-match-case" in s
    assert "'member-select-case':memberSelectCase" in s


def test_final_approval_continues_to_delivery_and_completion():
    s = source()
    assert "function adminDelivery" in s
    assert "'admin-delivery':adminDelivery" in s
    assert "배송 대기" in s
    assert "data-start-delivery" in s
    assert "배송 중" in s
    assert "data-complete-delivery" in s
    assert "m.status='완료'" in s


def test_offer_catalog_uses_thumbnail_feed_and_category_tabs():
    s = source()
    assert "thumbnail:'assets/offer-" in s
    assert 'class="offer-feed-item' in s
    assert 'class="offer-thumb"' in s
    assert 'class="offer-feed-copy"' in s
    assert "['전체','식사','물품','서비스']" in s
    assert "data-resource-category" in s
    assert "최신 등록순" in s


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
