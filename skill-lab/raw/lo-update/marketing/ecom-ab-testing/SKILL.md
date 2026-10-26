---
name: Framework A/B Testing Toàn Diện
description: >
  A/B testing methodology, setup, analysis cho TMĐT. Các yếu tố cần test (ads, landing page,
  email, checkout, pricing). Statistical significance, sample size, test duration, ICE score
  prioritization, 20 A/B test ideas sẵn chạy. Dùng khi cần: "A/B testing", "split test",
  "conversion optimization", "test hypothesis", "which version better", "optimize ads",
  "landing page test", "email subject line test"
---

# A/B TESTING FRAMEWORK - TOÀN DIỆN TMĐT

## TỔNG QUAN: TẠI SAO A/B TESTING QUAN TRỌNG

### Impact:
- 1% improvement × 365 days = 37% improvement/year
- Top e-commerce sites test 20+ variations per month
- Average ROAS improvement: 10-25% per quarter (with consistent testing)

### Reality of optimization:
```
Without testing:
"I think red button converts better"
→ Guessing → Wrong choice → Lost revenue

With A/B testing:
"I hypothesize red converts better"
→ Test → Validate → Scale winner → +5-10% conversion
```

---

## A/B TESTING METHODOLOGY: 5 STEPS

### STEP 1: HYPOTHESIS (Xác định giả thuyết)

**Structure:**
```
"If [change X],
then [result Y will improve],
because [reason Z]"
```

**Examples:**
```
✓ "If I change button color from blue to red,
  then click-through rate will increase by 10%,
  because red creates urgency"

✓ "If I simplify checkout from 5 steps to 1 page,
  then checkout completion rate will improve by 20%,
  because fewer steps = less friction"

✓ "If I add social proof testimonial above fold,
  then conversion rate will increase by 8%,
  because testimonials build trust"
```

**Bad hypotheses:**
```
❌ "Make button red" (No hypothesis, no expected result)
❌ "Everything is a problem" (Unfocused)
❌ "Our competitor does it, so it's better" (No reasoning)
```

### STEP 2: DESIGN (Thiết kế test)

**A/B test structure:**

```
CONTROL (A) = Current version (baseline)
TREATMENT (B) = New version (what we're testing)

Change only 1 variable (to isolate impact)

Example:
Control: Blue button + "Buy now"
Treatment: Red button + "Buy now"
(Only change: color)

NOT:
Control: Blue button + "Buy now"
Treatment: Red button + "Claim your deal" (color + copy)
→ Can't tell which caused improvement
```

### STEP 3: RUN (Chạy test)

**Elements:**
1. **Sample size**: Enough visitors per variant
2. **Duration**: Minimum test period
3. **Traffic split**: Usually 50/50, can be 70/30

**Sample size calculator:**

Rule of thumb:
- Need minimum 100-200 conversions per variant
- Faster conversion = need less time
- E-commerce: Usually 1-2 weeks

Formula (simplified):
```
Sample size = (Z-score² × P(1-P)) / (Effect size)²

Where:
- Z-score = 1.96 (95% confidence)
- P = baseline conversion rate (e.g., 0.05 = 5%)
- Effect size = minimum improvement to detect (e.g., 0.10 = 10% relative improvement)

Example:
Baseline conversion: 5%
Want to detect: 10% relative improvement (5% → 5.5%)
Result: Need ~3000 visitors per variant
```

**Test duration:**

Minimum:
- 7 days (to capture weekly patterns)
- 100 conversions per variant (whichever is longer)

Maximum:
- Stop at significance (don't keep running if winner is clear)
- Don't run >4 weeks (external factors change, market shifts)

**Sample test calendar:**
```
Week 1: Launch test, monitor for bugs
Week 2: Check results, ensure we have enough sample
Week 3-4: Hit statistical significance
Decide winner + implement
```

### STEP 4: ANALYZE (Phân tích kết quả)

**Key metric: Statistical Significance**

Definition: Probability that result is NOT due to chance (usually 95% confidence = p-value < 0.05)

**Simple interpretation:**
```
If A: 5% conversion, B: 5.5% conversion
Sample: 5000 per variant

Question: Is 0.5% improvement real or luck?

Tool shows: "Winner B with 96% confidence"
→ Only 4% chance this is luck → STATISTICALLY SIGNIFICANT
→ Safe to implement

Tool shows: "Winner B with 70% confidence"
→ 30% chance this is luck → NOT STATISTICALLY SIGNIFICANT
→ Run longer or different variant
```

**Tools for analysis:**
- Google Optimize (built-in analytics)
- VWO (Visual Website Optimizer)
- Optimizely
- Facebook A/B test tool
- TikTok Ads A/B test
- Shopee A/B test (native)

**What to measure:**
- Primary metric: What you're optimizing for (conversion rate, clicks, etc)
- Secondary metrics: Related metrics that might be affected
- Negative metrics: Watch for unintended consequences

Example:
```
Test: Make CTA button bigger
Primary: Click-through rate ↑15% ✓
Secondary: Scroll-down rate ↑ (more clicks = more scrolling)
Negative watch: Bounce rate (didn't increase) ✓
→ Overall: Good change, implement
```

### STEP 5: IMPLEMENT & ITERATE (Triển khai & Lặp lại)

**Decision framework:**

```
If statistical significance ✓ AND practical significance ✓:
→ IMPLEMENT: Roll out to 100% traffic

If statistical significance ✓ but practical significance ✗:
→ ARCHIVE: Won, but improvement too small to matter
→ Move to next test

If statistical significance ✗:
→ REJECT: Not enough evidence, run longer or test different variant

If unexpected negative result:
→ INVESTIGATE: Maybe population-specific effect
→ Test again with different segment
```

**After implementation:**
- Monitor for 1-2 weeks
- Ensure results hold (no degradation)
- Document learnings
- Move to next hypothesis

---

## WHAT TO A/B TEST IN TMĐT

### CATEGORY 1: ADS (Facebook, Google, TikTok)

**1. Headline variations**
```
A: "Áo khoác Nike sale 50%"
B: "Áo khoác Nike - Bí quyết mà 99% shop không biết"

Test: Which gets better CTR?
```

**2. Image vs Video**
```
A: Static product image
B: 15-second video demo

Test: Which has higher conversion rate?
```

**3. CTA button text**
```
A: "Learn more"
B: "Buy now"

Test: Which drives more conversions?
```

**4. Audience targeting**
```
A: Broad audience (18-65, interest: "Fashion")
B: Narrow audience (25-35, past website visitors)

Test: Which has better ROAS?
```

**5. Placement**
```
A: Instagram feed
B: Instagram stories

Test: Which platform performs better for this ad?
```

**6. Budget allocation**
```
A: 50/50 split between two audiences
B: 70/30 split (put more budget where converting better)

Test: Dynamic budget allocation = better ROAS?
```

**7. Copy length**
```
A: Long ad copy (3-4 sentences)
B: Short ad copy (1 sentence)

Test: Which gets better engagement?
(Note: Depends on platform. Short = social, Long = email)
```

---

### CATEGORY 2: LANDING PAGE

**8. Hero headline**
```
A: "Áo khoác Nike chính hãng 100%"
B: "Hết mụn trong 14 ngày, hoặc hoàn tiền"
(Note: Change to match your product)

Test: Which headline gets more form submissions?
```

**9. Hero image**
```
A: Product on white background
B: Product on lifestyle background (person wearing it)

Test: Which increases conversion?
```

**10. CTA button color**
```
A: Blue button
B: Red button
C: Green button (optional 3-way test)

Test: Which button color gets most clicks?
```

**11. Form fields**
```
A: 5 fields (name, email, phone, company, message)
B: 3 fields (name, email, message)

Test: Fewer fields = more form completions?
```

**12. Trust signals placement**
```
A: Trust signals scattered (testimonials in middle, ratings at bottom)
B: Trust signals clustered at top (all above fold)

Test: Which placement builds more trust → higher conversion?
```

**13. Pricing display**
```
A: "$100/month"
B: "$3.33/day" (same price, different framing)

Test: Which pricing framing gets more signups?
```

**14. Video presence**
```
A: No video
B: Explainer video above fold

Test: Does video increase time-on-page + conversion?
```

---

### CATEGORY 3: EMAIL

**15. Subject line**
```
A: "New product release"
B: "[Name], limited-time offer inside 👇"

Test: Which subject has higher open rate?
```

**16. Send time**
```
A: 9 AM
B: 7 PM

Test: Which time drives better click rate?
(Varies by audience)
```

**17. Email length**
```
A: Short email (2-3 paragraphs, 1 image)
B: Long email (5+ paragraphs, 3 images, multiple stories)

Test: Which email gets higher conversion rate?
(Note: Depends on product, audience)
```

**18. CTA copy in email**
```
A: "Learn more"
B: "Get your copy today"

Test: Which CTA text gets more clicks?
```

**19. From name**
```
A: "sales@shop.com"
B: "Hương from Shop Vanity"

Test: Personalized from name = higher open rate?
```

---

### CATEGORY 4: CHECKOUT

**20. Cart page layout**
```
A: Product list on left, summary on right
B: Product list taking full width, summary below

Test: Which layout increases conversion?
```

**21. Upsell placement**
```
A: No upsell on cart page
B: "Frequently bought together" section on cart

Test: Does upsell opportunity increase AOV?
```

**22. Trust badges on checkout**
```
A: No trust badges
B: SSL badge + guarantee + support chat visible

Test: Does showing security increase checkout completion?
```

**23. Payment method default**
```
A: Credit card pre-selected
B: COD (cash on delivery) pre-selected

Test: Which default increases checkout completion?
(In VN, COD likely wins)
```

---

## PRIORITIZATION: ICE SCORE METHOD

**When to run which test?**

Don't test everything at once. Prioritize using ICE score:

```
ICE = (Impact × Confidence × Ease)

Impact (1-10): How much will this improve metrics?
- 10 = Game-changer
- 5 = Moderate improvement
- 1 = Minimal improvement

Confidence (1-10): How confident are we this will work?
- 10 = Strong evidence (competitors do it, data shows it)
- 5 = Moderate confidence (logical, but unsure)
- 1 = Low confidence (just guessing)

Ease (1-10): How easy is it to implement?
- 10 = Trivial (change button color)
- 5 = Moderate (requires design change)
- 1 = Difficult (requires backend change)
```

**Examples:**

```
Test A: Change button color red to blue
Impact: 5 (might help, might not)
Confidence: 6 (some evidence)
Ease: 10 (trivial)
ICE Score: 5 × 6 × 10 = 300 ← Run this (easy, quick)

Test B: Redesign entire checkout flow
Impact: 9 (huge potential improvement)
Confidence: 7 (good evidence)
Ease: 2 (requires backend, design, QA)
ICE Score: 9 × 7 × 2 = 126 ← Run later (high impact but expensive)

Test C: Add testimonial section
Impact: 7 (good impact on trust)
Confidence: 8 (strong evidence)
Ease: 8 (easy to add)
ICE Score: 7 × 8 × 8 = 448 ← Run this (good all around)
```

**Priority roadmap:**
1. Run highest ICE score tests first
2. Quick wins (high ease, high impact)
3. Strategic bets (high impact, medium ease)
4. Later: Long-term infrastructure changes

---

## 20 A/B TEST IDEAS SẴN CHẠY

### For all e-commerce:

**Test 1: Hero CTA button color**
```
A: Blue
B: Red
Expected winner: Red (creates urgency)
Duration: 1 week
Priority: High (quick, easy)
```

**Test 2: Add testimonial above fold**
```
A: No testimonial
B: Customer testimonial + 5-star rating visible immediately
Expected winner: B (social proof)
Duration: 1 week
Priority: High
```

**Test 3: Headline variation**
```
A: "Premium [product]"
B: "Bí mật mà 99% người không biết"
Expected winner: Depends on audience
Duration: 2 weeks
Priority: Medium
```

**Test 4: Checkout steps**
```
A: 3-step checkout
B: 1-page checkout
Expected winner: B (less friction)
Duration: 1-2 weeks
Priority: High
```

**Test 5: Payment method default**
```
A: Credit card default
B: COD (cash on delivery) default
Expected winner: B in Vietnam
Duration: 1 week
Priority: Medium
```

**Test 6: Add video to product page**
```
A: Product image only
B: Product video + image
Expected winner: B (video increases time-on-page)
Duration: 2 weeks
Priority: Medium
```

**Test 7: Upsell on cart page**
```
A: No upsell
B: "Frequently bought together" section
Expected winner: B (increases AOV)
Duration: 2 weeks
Priority: Medium
```

**Test 8: Free shipping messaging**
```
A: Hidden in checkout (appears at last moment)
B: Prominent at cart page ("Freeship if you spend 300k+")
Expected winner: B (encourages larger orders)
Duration: 1-2 weeks
Priority: High
```

**Test 9: Email subject line**
```
A: "Flash sale - 24 hours only"
B: "[Name], 50% off your favorite items"
Expected winner: Depends, usually B (personalization)
Duration: 1 email send
Priority: High (low cost)
```

**Test 10: Ad headline**
```
A: "Buy [product] now"
B: "[Product] - Try risk-free for 30 days"
Expected winner: B (removes risk)
Duration: 1 week
Priority: High
```

**Test 11: Product image angle**
```
A: Product from front
B: Product from lifestyle angle (person using it)
Expected winner: B (shows use case)
Duration: 1-2 weeks
Priority: Medium
```

**Test 12: Form length**
```
A: 5 form fields
B: 3 form fields
Expected winner: B (less friction)
Duration: 1 week
Priority: High
```

**Test 13: Discount framing**
```
A: "50% off"
B: "Buy 1 get 1 50% off"
Expected winner: Depends on product
Duration: 1-2 weeks
Priority: Medium
```

**Test 14: Newsletter signup**
```
A: No incentive ("Sign up for updates")
B: With incentive ("Sign up, get 50% off")
Expected winner: B (incentive drives more signups)
Duration: 2 weeks
Priority: High
```

**Test 15: Trust signals combination**
```
A: Just price + image
B: Price + image + testimonial + guarantee badge
Expected winner: B (multiple trust signals)
Duration: 1-2 weeks
Priority: High
```

**Test 16: CTA copy on button**
```
A: "Learn more"
B: "Claim your deal"
Expected winner: B (more action-oriented)
Duration: 1 week
Priority: High
```

**Test 17: Shipping cost display**
```
A: "Shipping: +50k"
B: "Shipping: Calculated at checkout"
Expected winner: Depends, B hides cost until later
Duration: 1-2 weeks
Priority: Medium
```

**Test 18: Social proof counter**
```
A: No counter
B: "[X] people bought this today" (social proof)
Expected winner: B (FOMO effect)
Duration: 2 weeks
Priority: Medium
```

**Test 19: Email send time**
```
A: 9 AM
B: 7 PM
Expected winner: Usually B (evening engagement)
Duration: 1 send cycle
Priority: Medium (test with 1 email, then optimize)
```

**Test 20: Checkout progress indicator**
```
A: No progress bar
B: Progress bar showing "Step 2 of 3"
Expected winner: B (reduces anxiety)
Duration: 1 week
Priority: High
```

---

## COMMON A/B TESTING MISTAKES

### Mistake 1: Testing multiple variables at once
```
❌ Change button color + copy + size simultaneously
→ Can't tell which caused improvement

✓ Change only button color
→ Clear cause & effect
```

### Mistake 2: Stopping test too early
```
❌ After 3 days, one version has 60% CTR, stop test
→ Not enough sample size, result could be luck

✓ Run until statistical significance (usually 7-14 days)
→ Ensure result is real
```

### Mistake 3: Ignoring statistical significance
```
❌ "Version B got 5% more conversions, let's use it"
→ Could be 95% chance this is luck

✓ Use p-value < 0.05 (95% confidence)
→ Only 5% chance this is luck
```

### Mistake 4: P-hacking (testing until you win)
```
❌ Test 10 variations, pick the one that "won"
→ With 10 tests, one is likely to "win" by chance (false positive)

✓ Pre-define hypothesis + test duration before running
→ Stick to plan
```

### Mistake 5: Not considering external factors
```
❌ Start test Tuesday, competitor launches big sale Thursday
→ Results skewed by external event

✓ Track external events
→ Acknowledge impact in analysis
```

### Mistake 6: Implementing without monitoring
```
❌ Implement winning test 100% traffic, don't monitor
→ Might have negative side effects you didn't notice in test

✓ Monitor for 1-2 weeks after implementation
→ Ensure results hold
```

---

## TESTING ROADMAP TEMPLATE

### Month 1:
```
Week 1: Button color test (Blue vs Red)
Week 2: Headline test (A vs B)
Week 3: Testimonial placement test
Week 4: Form field test (5 vs 3 fields)

Expected impact: 5-8% overall conversion improvement
```

### Month 2:
```
Week 1: Checkout flow test (3-step vs 1-page)
Week 2: Upsell test
Week 3: Email subject line test (A vs B)
Week 4: Trust signals test

Expected impact: 8-12% improvement
```

### Month 3:
```
Week 1: Payment method default test
Week 2: Image vs lifestyle photo test
Week 3: Video on product page test
Week 4: Freeship messaging test

Expected impact: 10-15% improvement
```

### Cumulative improvement:
```
5% × 1.08 × 1.10 × 1.12 = ~6.7% improvement from 3 months of testing
Seems small, but compounds over time and across all pages
```

---

## A/B TESTING TOOLS

| Tool | Best For | Cost | Features |
|------|----------|------|----------|
| Google Optimize | Website | Free (with GA4) | Free, native integration |
| Facebook A/B test | Ads | Free | Built-in to ads manager |
| TikTok A/B test | TikTok ads | Free | Campaign-level testing |
| VWO | Landing pages | Paid | Visual editor, analytics |
| Optimizely | Enterprise | Paid | Advanced segmentation |
| Unbounce | Landing pages | Paid | Template builder |
| ConvertKit | Email | Free/Paid | A/B subject lines |
| HubSpot | Email | Free/Paid | A/B test automation |

---

## TESTING CHECKLIST

Before launching test:
- [ ] Hypothesis documented
- [ ] Single variable being tested
- [ ] Sample size calculated
- [ ] Test duration planned (min 7 days)
- [ ] Primary metric defined
- [ ] Statistical significance target set (95% confidence)
- [ ] Tool set up correctly
- [ ] Team aware of test (don't change things mid-test)

During test:
- [ ] Monitor for obvious bugs
- [ ] Check tracking is working
- [ ] Note any external events (sales, news, etc)

After test:
- [ ] Check statistical significance
- [ ] Document results (win/loss/inconclusive)
- [ ] Document learnings
- [ ] Implement winner if significant
- [ ] Move to next test

---

## RESULTS DOCUMENTATION TEMPLATE

### Test [#1]: [Name]

**Hypothesis:**
"If [change X], then [result Y], because [reason Z]"

**Test period:** [Dates]
**Sample size:** [# per variant]
**Primary metric:** [What we measured]

**Results:**
```
Control (A): 5.2% conversion rate (1,234 conversions / 23,700 visitors)
Treatment (B): 5.8% conversion rate (1,389 conversions / 23,900 visitors)
Improvement: +0.6% relative (11% relative improvement)
Statistical significance: 94% (p = 0.06)
```

**Conclusion:** INCONCLUSIVE - Not quite statistically significant (need 95%). Run longer or with more traffic.

**Next step:** Rerun with larger sample or test different variation.

**Learnings:**
- Direction was positive (B > A)
- Effect size smaller than expected
- Consider combining with other improvements

