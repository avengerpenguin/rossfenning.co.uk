Title: Authorisation vs. Authentication and why we should care
Date: 2010-06-15 19:37
Slug: authorisation-vs-authentication
Category: Security
Tags: authentication, authorisation, security, identity
Author: Ross Fenning

At some point whilst interacting with many websites or web-based
applications and services, users are asked to state and prove who they
are. Whether this is to make sure only that user edits their own profile
or it is for secure financial transactions, identity, trust and
authorisation underpin almost any secure communication. Here, I will
break down the basic, distinct components of user identification and
show why the distinction between them is important for designing or even
using a secure system.

Defining the Difference
-----------------------

The first division — and the one discussed in this post — is the
difference between the process of authentication and that of
authorisation. Given that many people use one term to cover both
processes, the distinction might seem pedantic, but understanding the
divide can greatly improve the user-friendliness and security of an
application. Authentication can be said to be broken down into trust and
identity, but that will be discussed in another post.

In short, authentication is the act of getting a person to say who they
are and then to confirm they are indeed that person. In contrast,
authorisation already assumes that individual is who they say they are,
but goes further to confirm they are permitted to see the resource or
perform the action they are requesting. In essence, this breaks down a
login process into two questions:

1.  Who is this person?
2.  What may this person see or do?

A suitable analogy here can be made with credit card purchases in a
shop. Signing a receipt — assuming it matches that on the back of your
card — or entering your PIN into a [Chip and
PIN](http://www.chipandpin.co.uk/) device is the authentication process.
The assumption is that only the true card owner would normally be able
to replicate the signature or know the corresponding PIN, but this still
does not guarantee the transaction will continue through to completion.

This is because the next and final step is for the bank to be contacted
to decide whether you actually have enough funds or credit remaining to
make the purchase. Here, the bank is happy that the user's identity has
already been confirmed by signature or PIN and it is only concerned with
authorising the desired request for funds.

Authentication and Authorisation in Web Applications
----------------------------------------------------

When designing the flow of an application, the best user experience
comes from only authenticating once, but authorising on every request
after that. A large number of applications achieve this by asking the
user to login before the first privileged request and then storing their
login into a session or cookie. No sensible website asks a user to log
in again every time they do anything.

Note the distinction coming into play in that all future requests will
assume that cookie or session is truthful when it asserts which user is
currently logged in. This highlights a very important part of security
where it should not be possible for a malicious person to forge the
necessary information to claim they are already logged in as user.

For developers, this means storing a random [session
ID](http://en.wikipedia.org/wiki/Session_ID) in the cookie after login
as opposed to storing the user ID, which can be forged easily.

What about the experience for the user? There is a good reason why the
[HTTP response
codes](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) have the
distinction of "401 Unauthorized" and "403 Forbidden". Annoyingly, even
the HTTP specification itself here is using the terms authorisation and
authentication interchangeably. More accurate would be to call the
former "401 Not authenticated" and the latter "403 Not authorised".

The reason for this is that the 401 response is telling the user or web
browser that this particular resource cannot be accessed by just anyone
and you are expected to come back with proof of identity. The most
common outcome here is that the web browser will display a box asking
for a username and password and will then send those over automatically
without the user necessarily knowing the exact process behind the
scenes.

Once the user is logged in, the website is still normally going to do
the authorisation process to check that the authenticated user is
permitted to see or do this exact resource or action, e.g. I may be
logged into Facebook as a valid user, but I should not be permitted to
edit another user's profile. If the user is permitted, they get the page
they wanted successfully — normally HTTP status code 200 "OK" — but if
they are still not allowed to be here, they get the "403 Forbidden"
response.

### Corporate and University Networks

This duality of authentication and authorisation plays out very strongly
in a large environment such as a corporation or a university. Most
enterprise-level computer networks in these institutions will have a
central user directory that can be consulted whenever anybody wants to
log in to a computer, a web application or any other system that needs
to be secured.

Whilst every system will contact the same user directory, it is very
unlikely that all users will have access to everything. Senior managers
may have sole access to the most confidential company data or a
university may have internal systems only accessible by staff and not
students. Some resources may be restricted to certain departments only.

To this end, all systems and applications are going to perform a
two-step process — just as with credit card purchases — before allowing
a user access. The first will be to authenticate their username and
password and the second will be to check extra information about the
user to confirm they are authorised to have access. Generally, user
directories will have extra attributes about each user such as
department and allow the administrators to put people into other custom
groups that reflect however people may be grouped together in the
organisation. For example, a user may have to be in the "Payroll" group
to access the payroll system.

Most applications will internalise this two-step procedure so it appears
to the user as only one step from entering login details and gaining
access to the system. In light of this, why discuss the
authentication/authorisation distinction at all here? The reasons are
two-fold.

The first consideration is user-friendliness of the login process. If
the only two outcomes of a login attempt are success (access is granted)
or failure (access is not granted), the user is none the wiser as to
whether they entered their password incorrectly or whether they are not
sufficiently privileged enough to be allowed into this system. A less
frustrating set of outcomes would be success, Not Authenticated and Not
Authorised.

Here, the application is explaining which of the two steps went wrong
for the user. If the authentication stage failed, then the user can be
returned back to the login page with a message saying their login
details were not recognised (so the user can try their password again or
contact IT support to see if their account was suspended/removed for any
reason). If the problem lay in the authorisation step, then the user can
be informed there was nothing wrong with their password and present a
more helpful message including details of how to gain access to this
system if they believe they should have it. This is normally a more
administrative task of adjusting their user account to be in the correct
group rather than a technical fault.

The second issue concerns user-friendliness as well, but is more about
fighting a problem that arises in any large organisation that has
several computer systems. For example, an employee of a payroll
department may come into to work each morning, log in to their PC and
throughout the day have to log in again to:

-   the payroll system,
-   the HR system to book holidays,
-   the room booking system to request meeting rooms,
-   their email,
-   the finance system to claim business expenses or
-   the company [intranet](http://en.wikipedia.org/wiki/Intranet)

Whilst having a central user directory for all these systems to consult
for verifying usernames and passwords means this employee only has to
remember one password (and if they change it, it changes for all systems
in one go), it does not save them from having to type it in several
times in one day. This is because it is common for corporate systems to
have their own individual login pages that link up to your user
directory, but still each perform both steps of authentication and
authorisation individually as well.

Single Sign-on
--------------

Anything designed as a solution to the aforementioned problem is known
as Single sign-on or SSO as it is commonly called. An SSO setup within
an organisation will ensure the user only types their username and
password in once — per day, usually — and that action is then propagated
to all systems who then trust the fact that the user has already
identified themselves.

More abstractly, this is a setup where all the applications no longer do
the authentication step and instead go straight to the authorisation
step. The authentication process has been moved out to a single login
page/screen and there exists some mechanism by which the login process
passes over to these applications the name of the person that has been
logged in.

It can be thought of as a building with a single security desk at the
front. People entering the building are asked to show ID and are then
issued with a security card valid for that day which allows them to
access areas of the building they are permitted to enter as freely as
they like. This card contrasts the cumbersome approach of having an ID
checkpoint at every door in the building.

The drawback with this setup is that many commercial applications are
not designed to integrate nicely with many SSO systems, but it is
certainly simple to build support into any applications developed within
the organisation. Many people who have experienced higher education will
have already used an SSO setup if they have used any of the following:

-   Athens,
-   Shibboleth,
-   Webauth (Built at [Stanford](http://stanford.edu/) and used at
    [Oxford](http://www.ox.ac.uk/)) or
-   [Raven](https://raven.cam.ac.uk/) at
    [Cambridge](http://www.cam.ac.uk)

With Athens or Shibboleth, students are asked to log in whenever they
wish to access an external, educational resource for which their
university is paying a licence, but — so long as they do not close their
browser — are not asked to do so again even if they proceed to view
other resources they are also permitted to access. It is entirely
possible to merge this with an internal SSO system so that the moment a
user logs into anything once, they have an unhindered pass to browse all
permitted resources, internal or external.

A comparison of technical solutions for SSO will be discussed in a
future post.

Duality
-------

Despite the important distinction between the two processes of
authentication and authorisation, they do remain a tightly-coupled pair
in a security system. Authorisation is meaningless without a proper
authentication procedure that can be trusted to verify people's identity
accurately. For example, imagine a credit card transaction that
authorised funds for a purchase without the buyer having signed anything
nor entered their PIN.

Further Considerations
----------------------

In this post, the authentication process was assumed mostly to be the
recognisable username and password combination. What has not been
discussed is:

-   how we give those out in the first place;
-   how we protect them from being stolen;
-   other forms of proving yourself (swipe cards, fingerprints, etc.);
    or
-   the concept of identity vs. trust (two constituent parts of
    authentication).

These will be addressed in a future post. Also, there will be another
article to show how the same theory behind authentication is important
for the reverse process of a user verifying a website is who it claims
to be, e.g. that you are looking at your bank's legitimate website and
not an imitation set up to steal your account details.
