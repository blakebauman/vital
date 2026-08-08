# Show HN

Reference for the `press-kit` skill. Show HN (`https://news.ycombinator.com/showhn.html`) is the one launch surface where the audience is hostile to marketing by design, so it is worth more than a paragraph of generic "post to HN" advice. Read the [Show HN rules](https://news.ycombinator.com/showhn.html) and the [site guidelines](https://news.ycombinator.com/newsguidelines.html) before drafting; they change rarely but they are the authority, not this file.

## 1. Qualify before you draft

Show HN is for **something you made that other people can play with**. Run the gate before writing a single line of copy, and give the client a straight verdict.

Qualifies:

- Software people can use or run right now.
- Hardware, if there's a video or article showing it working.
- A book, if there's a sample chapter.
- A genuine, substantial overhaul of an existing project.

Does not qualify — the rules name these as off-topic:

- Blog posts, sign-up pages, newsletters, lists, and other reading material.
- Anything that is only a landing page or a waitlist.
- Routine version bumps and incremental releases.

Two more disqualifiers that are not rules but are reliably fatal:

- **A demo behind a signup wall.** The rules ask you to make it easy to try without barriers such as signups or emails. A launch that opens with an email gate gets its top comment about the email gate.
- **Nothing technically interesting.** HN's readership is engineers. A CRUD app with a nice UI and no interesting decision behind it gets ignored, not attacked.

If the client fails the gate, say so plainly and redirect: ship the thing that qualifies first, post an "Ask HN" or a technical write-up as a regular submission instead, or use Product Hunt and niche communities where a polished-but-ordinary product does fine. Posting anyway is worse than not posting — a flagged or ignored Show HN burns the one clean shot.

## 2. The title

Format: `Show HN: <plain description of the thing>`. That is the whole formula.

- No exclamation points, no uppercase for emphasis, no linkbait — the guidelines call this out directly.
- No company name padding, no tagline, no "the future of". `Show HN: A CLI that diffs two Postgres schemas` beats `Show HN: SchemaSync – Effortless Database Migrations for Modern Teams`.
- Say what it *is*, not what it *does for you*. Nouns over benefits.
- Keep it short — HN's title field caps at 80 characters, and short titles read better on the front page anyway.
- If it's an unusual implementation, the implementation is often the better title: `Show HN: I wrote a BitTorrent client in 500 lines of Rust`.

Write three or four candidate titles and pick with the client. The title does most of the work.

## 3. The link and the demo

The URL should land on the thing itself, not a marketing page about the thing. Before posting, check:

- It works with no account, or there's an obvious no-signup demo path.
- It works on mobile — a large share of the first traffic is people on phones.
- It survives load. The front page is a real traffic spike; know what falls over and have static fallbacks or caching ready.
- Pricing, if any, is visible and honest. Hiding that it's paid reads as a bait and switch and the thread will say so.
- Licensing and "open source" claims are accurate. HN checks.

## 4. The text and the first comment

**The founder writes this, not Vital.** HN's comment guidelines ask people not to post AI-generated or AI-edited text, and the thread's whole value is that a real maker is answering. So the deliverable here is *not* pasteable prose — it's a brief the founder writes from.

Give the client:

- The four or five things the comment must cover, in order.
- The specific facts to include, pulled from the workspace.
- A list of what to cut.

What the first comment should cover:

1. **What it is and what problem it solves**, in two sentences, concretely.
2. **Why you built it** — the actual itch. Personal motivation reads well here and nowhere else.
3. **How it works** — the interesting technical decision. This is the part HN reads. Name the stack, the tradeoff you made, the thing that was harder than expected.
4. **What it doesn't do yet** — stated before someone else finds it. Honesty about limits buys enormous credibility in this thread.
5. **What feedback you want**, specifically.

What to cut: adjectives, "excited to share", "revolutionize", growth-hacky asks, anything that sounds like a press release, and any claim you can't back in a reply. Business model questions come up constantly — decide the honest answer in advance rather than improvising it in the thread.

## 5. Timing and posting

- Post it yourself, from the account of someone who actually built it, and be at a keyboard for the next few hours.
- Weekday mornings US Eastern are the conventional window. Treat it as a mild effect, not a strategy — Show HN posts sit on `/show` and `/shownew` and get seen regardless of the exact hour.
- Never launch and walk away. An unanswered Show HN dies.
- Don't coordinate with a Product Hunt launch to the same hour if it means the founder can't give the HN thread full attention. HN needs presence; Product Hunt needs a first comment and periodic replies. Sequence, don't overlap.

## 6. Working the thread

The first two hours decide it. The job is answering, not defending.

- Reply to every substantive comment. Short, direct, technical.
- Answer criticism head-on and concede what's true. "You're right, that's a real limitation, here's why I shipped anyway" outperforms every rebuttal.
- Skip the gratuitously negative ones. The guidelines discourage them, they still happen, and engaging costs you the room.
- Don't argue about downvotes, don't complain about the reception, don't accuse the thread of missing the point.
- Bug reports in the thread are free QA. Fix the quick ones live and say you did — that plays extremely well.
- Never edit the post to spin the reception.

## 7. Hard prohibitions

These are not tone advice; they are rules that get accounts and domains banned, and Vital does not help with any of them:

- **No asking for upvotes or comments.** Not friends, not Slack groups, not "we all upvote each other" founder rings. The guidelines forbid soliciting votes and HN's moderators actively detect voting rings.
- **No sock puppets or seeded comments.** Multiple accounts in your own thread is the fastest way to a permanent ban.
- **No delete-and-repost** to reset a bad start, and no resubmitting something that was killed.
- **No AI-written comments** posted as the founder's own words.

If a client asks for any of this, refuse it specifically, name the consequence, and offer the honest substitute — ask people who genuinely use the product to look at it and say what they actually think, in their own words, whenever they get to it.

## 8. When it flops

Most Show HNs get modest attention. That is the normal outcome, not a failure of the copy.

- Don't delete it. Deletion followed by a repost is against the rules and is visible.
- HN's own rule: if a story has not had significant attention in the last year or so, a small number of reposts is ok. So a single, later, honest repost — ideally with a better title or after a real change to the product — is legitimate. A same-week repost is not.
- HN moderators sometimes give overlooked good submissions a second chance on the front page. This is not something you can request; build nothing on it.
- Judge the outcome on the comments, not the points. Ten engineers telling you precisely why the abstraction is wrong is worth more than a front-page slot with no replies.

## What Vital delivers for a Show HN

- The qualify-or-don't verdict, stated first and plainly.
- Three or four candidate titles in the required format, with a recommendation.
- A pre-post checklist for the link, the demo path, and load.
- A **brief** for the first comment — points, facts, and cuts — explicitly for the founder to write in their own voice, with a note about why Vital isn't handing over pasteable text.
- A thread-handling plan: the first two hours, the three or four hardest questions the thread will ask, and the honest answer to each.
- The sequencing against Product Hunt and any press embargo.
