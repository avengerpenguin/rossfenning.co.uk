Title: Trust vs. Identity 
Date: 2010-07-15 18:42
Category: Security
Slug: trust-vs-identity
Tags: authentication, authorisation, trust, identity, security
Author: Ross Fenning

As stated in the [previous article about the difference between
authentication and authorisation](|filename|/authorisation-vs-authentication.md),
it is important to understand the different aspects of security in order
to control access to resources in as secure and as user-friendly a way
as possible. However, the step of authentication itself — the act of
ascertaining who a person is — comprises the two components of identity
and trust.

Authenticating an Identity
--------------------------

To return to the preceding article's example of credit card purchases in
a shop, the authentication step is where the retailer confirms your PIN
or signature before handing the transaction over to the bank for
authorisation.

The card has the owner's name printed across it, so the goal of the
authentication step is to prove that the person handing over the card is
indeed the owner. There are several possible approaches to proving
someone's identity, but we will look at the hand-written signature
approach for now.

Assuming for a moment that signature forgery isn't an issue, the theory
is that only the card's true owner could replicate the signature on the
back of the card. Thus the owner proves his or her identity by
reproducing said signature in front of the merchant.

Every time the card owner signs a receipt, we know that he or she is the
very same person that signed the back of the card in the first place.
More generally, identity is proving that a person matches the person
retained on record, e.g. that a user logging into the bank is the
account holder for the account they are trying to access.

Lack of Trust
-------------

There is however an Achilles' heel to this process. Comparing signatures
works on the assumption that the signature on the back of the card is
actually that of the card owner. If someone forgets to sign their card,
a thief can easily sign it with their own signature that they can
reproduce perfectly. Then any retailer will see that the signatures
match and that identity has been confirmed.

This is not an issue with the identification process, but an indication
of where trust has failed. Trust is an indication of whether the
identity has any validity in the first place. Interestingly, trust is
not always necessary in some applications, so it is worth understanding
the difference. Any security system that requires both identity and
trust should address each separately when analysing its strength.

Trust on the Web
----------------

If we look at the example of a general website with a registration and
login process, we can see identity and trust act differently in the
Internet realm.

Many websites ask users to sign up using an email address and a password
of their choosing. Once registration is complete, their email address
becomes their identity for coming back to the website at a later date.
Every time the user logs in with that email and password, we can be
happy it's likely to be the same person that first registered with those
details.

However, there are many ways this identity still lacks trust:

1.  we do not know that is actually their email address;
2.  we do not know this is a real person (it could be an automated
    process setting up accounts en masse); and
3.  we do not know other information such as their full name is
    accurate.

This is not necessarily a problem. If the website only deals with
storing and protecting a user profile, then the only concern is that the
person logging in is the same person that registered. This is a case
where we only care about identity and many websites merely require a
username and password just to record user activities against a profile.
They do not have a need for further information.

Some websites may require the that email address is valid at least for
the purposes of contacting or notifying the user. In these cases, some
trust is now required and most Internet users are already familiar with
having to confirm their email address by clicking a link that is emailed
to them after registration.

Other websites might confirm that a mobile number is valid by sending a
code by SMS or even that a postal address is accurate by sending a code
in the post (Google Adsense does this). When dealing with some UK
government online services, one may have to enter a passport number.
This is providing trust by cross-referencing the user-entered details
with that of another database.

Trusting Signatures
-------------------

To come back to the credit card purchase, banks attempt to introduce
trust by sending out new cards as securely as possible and then
encouraging customers to sign them immediately on arrival. They
generally also send new PINs separately. It is fair to assume most
customers do not want to be defrauded, so there is some trust in the
owner being the only one able to sign for a purchase or know the PIN.

Digital signatures can work on the web by having a mathematical key or
certificate attached to a file or email. The arithmetic involved can
prove that the signature attached matches exactly the key or certificate
you have recorded against that person or website's name, but we are
still faced with the original problem of proving legitimacy the first
time you encounter that key or certificate.

If I store my bank's certificate, I can use it to compare against the
certificate presented on future visits so that if looks different one
day, then it could well be criminals masquerading as my bank. This —
just as with comparing card signatures — falls foul to the the potential
illegitimacy of the original certificate.

Any computer file can be encrypted or certified by a digital key or
certificate. As digital keys and certificates can themselves be
represented as files, that means they can also sign other keys and
certificates. With this, many people can provide "trust networks" by
agreeing to sign the key of anyone they have met in real life. This
means you just need one key or certificate you are happy is legitimate
and you can trust any other ones signed by it. It then follows that you
can trust the ones signed by those as well and thus you end up with a
full web or chain of trust.

This is analogous to getting witnesses to sign a contract to confirm
that the signatory is indeed the right person. For the analogy to be
complete though, one would also have further witnesses signing to
confirm the signatures of the first witnesses are accurate as well. This
chain would continue until a signature is reached that is personally
recognised by the contract's author.

A similar approach is used for websites such as those of banks where
they have security certificates signed by one of a select number of
trustworthy certificate authorities. Most computer systems will
automatically trust the certificates of such known, legitimate
authorities and thus indirectly trust all certificates vouched for by
them. The security behind certificates used, web browsers and secure
websites will be discussed in fuller detail in a future article.

OpenID
------

OpenID is standardised protocol that allows web users to have a single
ID (from any OpenID provider) that they can use across several
websites. It addresses the difficulties of having to maintain identities
across multiple websites so long as a site is willing to accept an
OpenID identity as a valid login.

This provides a secure identity in that people will know that your
profile on one website is linked to that on any other website you use.
It makes it very difficult for someone to impersonate your identity at
any point.

However, it still does not provide trust (nor was it designed to do so)
and there is no way, for example, to say anything about the identity is
accurate, e.g. real name, company, email address.

Again, websites can still implement a registration process for OpenID
users not to provide them with a new identity, but to verify any further
details required. This allows the usual tactics of email verification,
etc. as discussed earlier. Another approach to asserting the validity of
users is to build a trust network on top of the OpenID system.

SAML, Shibboleth and the UK Federation
--------------------------------------

Another protocol by which people can use a single identity across
multiple websites is SAML. The best-known implementation of SAML is
Shibboleth, which is available both as an identity provider or a service
provider. The former allows one to set up a system that provides
identities, i.e. usernames, for people and the latter enables your
website to accept identities from the former.

For example, a university may wish to set up an identity provider to
give all the students some ID along the lines of user123@example.ac.uk
or http://example.ac.uk/user123 where "user123" is their username within
the institution. Then any service wishing to allow access to students
can implement itself as a service provider allowing users to log in with
their university ID.

This is certainly advantageous in that the service can automatically
enable access to all students from this example university without
having to ask each to register one by one and verify they are legitimate
students. Many students and former students may recognise this is as
similar to how Athens works in some universities.

So, not only does a Shibboleth service provider know that
user123@example.ac.uk is vouched for by the university, but there is
also trust that user123 is a real student — it is fair to assume this
university isn't giving out user accounts to people outside the
institution. This effects some trust because the service is able to know
something about this user and have confidence it is accurate.

If a user attempts to log in with user456@somewhereelse.com, the service
can reject them until whoever owns somewhereelse.com wants to pay for
its users to have access too. In this way, this service builds up a
trust network by listing institutions whose members may have access.

However, it is somewhat cumbersome if hundreds of different services
have to maintain manually a list of known educational institutions in
the UK. To make this simpler, many universities, colleges and companies
providing online resources thereto have become members of the [UK
Federation](http://www.ukfederation.org.uk/). This federation is
effectively a directory of known bodies and their details so it becomes
possible to configure a service simply to accept any identity within the
group knowing that they belong to a legitimate and accountable
institution.

The UK Federation can be seen as a trust network that attempts to build
upon the identification framework provided by SAML.

Whom to Trust
-------------

In essence, trust is inherited and passed on just as much in the
security world as in social interactions. Ultimately, it is necessary to
find a starting point that can be assumed trustworthy and then you can
trust anything it vouches for, just as one trusts business contacts
recommended by already trustworthy people.

As such, thumbprint identification is only useful if your thumbprint
database is accurate, passports are only good if you trust the
government that issued them and photo IDs in general only work if you
trust their resistance to forgery.

For any secure setup — whether web-based or in the physical world — it
is essential not only to verify the effectiveness of your identification
process, but also to ascertain the trustworthiness of the information
you are storing and using for identification in the first place.
