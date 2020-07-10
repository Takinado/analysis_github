import datetime
from unittest import TestCase

from models import Repository, Commit, Pull, Issue, DATETIME_FORMAT


class TestRepository(TestCase):
    def setUp(self):
        self.repo = Repository('path')
        date = datetime.datetime.now()
        raw_commits = [{
            'sha': '539f562bcbb319e01ce009ba6fc2f36f35ae0415',
            'node_id': 'MDY6Q29tbWl0Mjc0NDI5Njc6NTM5ZjU2MmJjYmIzMTllMDFjZTAwOWJhNmZjMmYzNmYzNWFlMDQxNQ==',
            'commit': {
                'author': {'name': 'Josh Holtz', 'email': 'josh@rokkincat.com', 'date': '2020-07-09T03:38:27Z'},
                'committer': {'name': 'GitHub', 'email': 'noreply@github.com', 'date': '2020-07-09T03:38:27Z'},
                'message': 'Version bump to 2.151.2 (#16806)',
                'tree': {
                    'sha': '554b14ea7018c2ce7abb181758a5063dad671ed4',
                    'url': 'https://api.github.com/repos/fastlane/fastlane/git/trees/554b14ea7018c2ce7abb181758a5063dad671ed4'},
                'url': 'https://api.github.com/repos/fastlane/fastlane/git/commits/539f562bcbb319e01ce009ba6fc2f36f35ae0415',
                'comment_count': 0,
                'verification': {
                    'verified': True, 'reason': 'valid',
                    'signature': '-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJfBpEzCRBK7hj4Ov3rIwAAdHIIAECdZhESDKs4G982J91uDSiL\nVRviYREuR5MrTIh1kRhY4+FfW0PBF5lmZdLCGmYngKVAhrXyaN4E8MOmlqlN8pfb\ngxE/WjIPFAq4F6IuszfZ01Uep75kfiXQgnt1HhHt5lnYHI2xlb2HOGi/b06AgH9q\n3XAIpbf8zSAcQE6d40oU6Lx4rP2aXkMJSm5GbXxm4ndWpd5NoqoNtIPlHF52ZOto\nvQ9k99A5fAs3V+TQf9zxVtyNEboZhJWTJt8JkpQoR/HU5Gfi5bo+ulD/LHuAWxFK\ne7esRQ24cR4Sw+gn7AnCwRfZLVKvj6+z2kEq00cbAA/HFEg16bPSqNkIfspemO8=\n=2q8j\n-----END PGP SIGNATURE-----\n',
                    'payload': 'tree 554b14ea7018c2ce7abb181758a5063dad671ed4\nparent f8931de7e0dd5e2189454725a671b7820744c29c\nauthor Josh Holtz <josh@rokkincat.com> 1594265907 -0500\ncommitter GitHub <noreply@github.com> 1594265907 -0500\n\nVersion bump to 2.151.2 (#16806)\n\n'}},
            'url': 'https://api.github.com/repos/fastlane/fastlane/commits/539f562bcbb319e01ce009ba6fc2f36f35ae0415',
            'html_url': 'https://github.com/fastlane/fastlane/commit/539f562bcbb319e01ce009ba6fc2f36f35ae0415',
            'comments_url': 'https://api.github.com/repos/fastlane/fastlane/commits/539f562bcbb319e01ce009ba6fc2f36f35ae0415/comments',
            'author': {'login': 'joshdholtz', 'id': 401294, 'node_id': 'MDQ6VXNlcjQwMTI5NA==',
                       'avatar_url': 'https://avatars2.githubusercontent.com/u/401294?v=4', 'gravatar_id': '',
                       'url': 'https://api.github.com/users/joshdholtz', 'html_url': 'https://github.com/joshdholtz',
                       'followers_url': 'https://api.github.com/users/joshdholtz/followers',
                       'following_url': 'https://api.github.com/users/joshdholtz/following{/other_user}',
                       'gists_url': 'https://api.github.com/users/joshdholtz/gists{/gist_id}',
                       'starred_url': 'https://api.github.com/users/joshdholtz/starred{/owner}{/repo}',
                       'subscriptions_url': 'https://api.github.com/users/joshdholtz/subscriptions',
                       'organizations_url': 'https://api.github.com/users/joshdholtz/orgs',
                       'repos_url': 'https://api.github.com/users/joshdholtz/repos',
                       'events_url': 'https://api.github.com/users/joshdholtz/events{/privacy}',
                       'received_events_url': 'https://api.github.com/users/joshdholtz/received_events',
                       'type': 'User',
                       'site_admin': False},
            'committer': {'login': 'web-flow', 'id': 19864447, 'node_id': 'MDQ6VXNlcjE5ODY0NDQ3',
                          'avatar_url': 'https://avatars3.githubusercontent.com/u/19864447?v=4', 'gravatar_id': '',
                          'url': 'https://api.github.com/users/web-flow', 'html_url': 'https://github.com/web-flow',
                          'followers_url': 'https://api.github.com/users/web-flow/followers',
                          'following_url': 'https://api.github.com/users/web-flow/following{/other_user}',
                          'gists_url': 'https://api.github.com/users/web-flow/gists{/gist_id}',
                          'starred_url': 'https://api.github.com/users/web-flow/starred{/owner}{/repo}',
                          'subscriptions_url': 'https://api.github.com/users/web-flow/subscriptions',
                          'organizations_url': 'https://api.github.com/users/web-flow/orgs',
                          'repos_url': 'https://api.github.com/users/web-flow/repos',
                          'events_url': 'https://api.github.com/users/web-flow/events{/privacy}',
                          'received_events_url': 'https://api.github.com/users/web-flow/received_events',
                          'type': 'User',
                          'site_admin': False},
            'parents': [{
                'sha': 'f8931de7e0dd5e2189454725a671b7820744c29c',
                'url': 'https://api.github.com/repos/fastlane/fastlane/commits/f8931de7e0dd5e2189454725a671b7820744c29c',
                'html_url': 'https://github.com/fastlane/fastlane/commit/f8931de7e0dd5e2189454725a671b7820744c29c'
            }]
        },
            {
                'sha': 'f8931de7e0dd5e2189454725a671b7820744c29c',
                'author': {'login': 'joshdholtz', },
            },
            {
                'sha': '9a434416f1f3b3d81f022ad5ff591dbe9d6a3a23',
                'author': {'login': 'CognitiveDisson', },
            }
        ]

        raw_pulls = [
            {  # open, not old
                'url': 'https://api.github.com/repos/fastlane/fastlane/pulls/16808', 'id': 446616460,
                'node_id': 'MDExOlB1bGxSZXF1ZXN0NDQ2NjE2NDYw',
                'html_url': 'https://github.com/fastlane/fastlane/pull/16808',
                'diff_url': 'https://github.com/fastlane/fastlane/pull/16808.diff',
                'patch_url': 'https://github.com/fastlane/fastlane/pull/16808.patch',
                'issue_url': 'https://api.github.com/repos/fastlane/fastlane/issues/16808', 'number': 16808,
                'state': 'open', 'locked': False,
                'title': 'add shortcuts for getting current pending release and current in revi…',
                'user': {'login': 'addbrick', 'id': 800916, 'node_id': 'MDQ6VXNlcjgwMDkxNg==',
                         'avatar_url': 'https://avatars1.githubusercontent.com/u/800916?v=4', 'gravatar_id': '',
                         'url': 'https://api.github.com/users/addbrick', 'html_url': 'https://github.com/addbrick',
                         'followers_url': 'https://api.github.com/users/addbrick/followers',
                         'following_url': 'https://api.github.com/users/addbrick/following{/other_user}',
                         'gists_url': 'https://api.github.com/users/addbrick/gists{/gist_id}',
                         'starred_url': 'https://api.github.com/users/addbrick/starred{/owner}{/repo}',
                         'subscriptions_url': 'https://api.github.com/users/addbrick/subscriptions',
                         'organizations_url': 'https://api.github.com/users/addbrick/orgs',
                         'repos_url': 'https://api.github.com/users/addbrick/repos',
                         'events_url': 'https://api.github.com/users/addbrick/events{/privacy}',
                         'received_events_url': 'https://api.github.com/users/addbrick/received_events', 'type': 'User',
                         'site_admin': False},
                'body': "…ew app store version\r\n\r\n<!-- Thanks for contributing to _fastlane_! Before you submit your pull request, please make sure to check the following boxes by putting an x in the [ ] (don't: [x ], [ x], do: [x]) -->\r\n\r\n### Checklist\r\n- [X] I've run `bundle exec rspec` from the root directory to see all new and existing tests pass\r\n- [X] I've followed the _fastlane_ code style and run `bundle exec rubocop -a` to ensure the code style is valid\r\n- [X] I've read the [Contribution Guidelines](https://github.com/fastlane/fastlane/blob/master/CONTRIBUTING.md)\r\n- [X] I've updated the documentation if necessary.\r\n\r\n### Motivation and Context\r\n<!-- Why is this change required? What problem does it solve? -->\r\nThis adds short cuts for getting the app store version which is In Review via `get_in_review_app_store_version`, and Pending Developer Release via `get_pending_release_app_store_version`. This way I don't have to remember the filters when looking these versions up.\r\n<!-- If it fixes an open issue, please link to the issue here. -->\r\n\r\n### Description\r\n<!-- Describe your changes in detail. -->\r\nThis adds short cuts for getting the app store version which is In Review via `get_in_review_app_store_version`, and Pending Developer Release via `get_pending_release_app_store_version`.\r\n<!-- Please describe in detail how you tested your changes. -->\r\n\r\n### Testing Steps\r\n<!-- Optional: steps, commands, or code used to test your changes. -->\r\n<!-- Providing these will reduce the time needed for testing and review by the fastlane team. -->\r\n",
                'created_at': (date + datetime.timedelta(days=-1)).strftime(DATETIME_FORMAT),
                'updated_at': '2020-07-09T04:54:19Z', 'closed_at': None,
                'merged_at': None, 'merge_commit_sha': '85cca3a26cd729e0ff480a2879fb3421a569006c', 'assignee': None,
                'assignees': [], 'requested_reviewers': [], 'requested_teams': [], 'labels': [
                {'id': 560540952, 'node_id': 'MDU6TGFiZWw1NjA1NDA5NTI=',
                 'url': 'https://api.github.com/repos/fastlane/fastlane/labels/cla:%20yes', 'name': 'cla: yes',
                 'color': '0e8a16', 'default': False, 'description': None}], 'milestone': None, 'draft': False,
                'commits_url': 'https://api.github.com/repos/fastlane/fastlane/pulls/16808/commits',
                'review_comments_url': 'https://api.github.com/repos/fastlane/fastlane/pulls/16808/comments',
                'review_comment_url': 'https://api.github.com/repos/fastlane/fastlane/pulls/comments{/number}',
                'comments_url': 'https://api.github.com/repos/fastlane/fastlane/issues/16808/comments',
                'statuses_url': 'https://api.github.com/repos/fastlane/fastlane/statuses/898998357e4e9953a0e800efda03f6debbee9ee9',
                'head': {'label': 'addbrick:brick/pending_developer_release', 'ref': 'brick/pending_developer_release',
                         'sha': '898998357e4e9953a0e800efda03f6debbee9ee9',
                         'user': {'login': 'addbrick', 'id': 800916, 'node_id': 'MDQ6VXNlcjgwMDkxNg==',
                                  'avatar_url': 'https://avatars1.githubusercontent.com/u/800916?v=4',
                                  'gravatar_id': '',
                                  'url': 'https://api.github.com/users/addbrick',
                                  'html_url': 'https://github.com/addbrick',
                                  'followers_url': 'https://api.github.com/users/addbrick/followers',
                                  'following_url': 'https://api.github.com/users/addbrick/following{/other_user}',
                                  'gists_url': 'https://api.github.com/users/addbrick/gists{/gist_id}',
                                  'starred_url': 'https://api.github.com/users/addbrick/starred{/owner}{/repo}',
                                  'subscriptions_url': 'https://api.github.com/users/addbrick/subscriptions',
                                  'organizations_url': 'https://api.github.com/users/addbrick/orgs',
                                  'repos_url': 'https://api.github.com/users/addbrick/repos',
                                  'events_url': 'https://api.github.com/users/addbrick/events{/privacy}',
                                  'received_events_url': 'https://api.github.com/users/addbrick/received_events',
                                  'type': 'User', 'site_admin': False},
                         'repo': {'id': 101232326, 'node_id': 'MDEwOlJlcG9zaXRvcnkxMDEyMzIzMjY=', 'name': 'fastlane',
                                  'full_name': 'addbrick/fastlane', 'private': False,
                                  'owner': {'login': 'addbrick', 'id': 800916, 'node_id': 'MDQ6VXNlcjgwMDkxNg==',
                                            'avatar_url': 'https://avatars1.githubusercontent.com/u/800916?v=4',
                                            'gravatar_id': '', 'url': 'https://api.github.com/users/addbrick',
                                            'html_url': 'https://github.com/addbrick',
                                            'followers_url': 'https://api.github.com/users/addbrick/followers',
                                            'following_url': 'https://api.github.com/users/addbrick/following{/other_user}',
                                            'gists_url': 'https://api.github.com/users/addbrick/gists{/gist_id}',
                                            'starred_url': 'https://api.github.com/users/addbrick/starred{/owner}{/repo}',
                                            'subscriptions_url': 'https://api.github.com/users/addbrick/subscriptions',
                                            'organizations_url': 'https://api.github.com/users/addbrick/orgs',
                                            'repos_url': 'https://api.github.com/users/addbrick/repos',
                                            'events_url': 'https://api.github.com/users/addbrick/events{/privacy}',
                                            'received_events_url': 'https://api.github.com/users/addbrick/received_events',
                                            'type': 'User', 'site_admin': False},
                                  'html_url': 'https://github.com/addbrick/fastlane',
                                  'description': '🚀 The easiest way to automate building and releasing your iOS and Android apps',
                                  'fork': True, 'url': 'https://api.github.com/repos/addbrick/fastlane',
                                  'forks_url': 'https://api.github.com/repos/addbrick/fastlane/forks',
                                  'keys_url': 'https://api.github.com/repos/addbrick/fastlane/keys{/key_id}',
                                  'collaborators_url': 'https://api.github.com/repos/addbrick/fastlane/collaborators{/collaborator}',
                                  'teams_url': 'https://api.github.com/repos/addbrick/fastlane/teams',
                                  'hooks_url': 'https://api.github.com/repos/addbrick/fastlane/hooks',
                                  'issue_events_url': 'https://api.github.com/repos/addbrick/fastlane/issues/events{/number}',
                                  'events_url': 'https://api.github.com/repos/addbrick/fastlane/events',
                                  'assignees_url': 'https://api.github.com/repos/addbrick/fastlane/assignees{/user}',
                                  'branches_url': 'https://api.github.com/repos/addbrick/fastlane/branches{/branch}',
                                  'tags_url': 'https://api.github.com/repos/addbrick/fastlane/tags',
                                  'blobs_url': 'https://api.github.com/repos/addbrick/fastlane/git/blobs{/sha}',
                                  'git_tags_url': 'https://api.github.com/repos/addbrick/fastlane/git/tags{/sha}',
                                  'git_refs_url': 'https://api.github.com/repos/addbrick/fastlane/git/refs{/sha}',
                                  'trees_url': 'https://api.github.com/repos/addbrick/fastlane/git/trees{/sha}',
                                  'statuses_url': 'https://api.github.com/repos/addbrick/fastlane/statuses/{sha}',
                                  'languages_url': 'https://api.github.com/repos/addbrick/fastlane/languages',
                                  'stargazers_url': 'https://api.github.com/repos/addbrick/fastlane/stargazers',
                                  'contributors_url': 'https://api.github.com/repos/addbrick/fastlane/contributors',
                                  'subscribers_url': 'https://api.github.com/repos/addbrick/fastlane/subscribers',
                                  'subscription_url': 'https://api.github.com/repos/addbrick/fastlane/subscription',
                                  'commits_url': 'https://api.github.com/repos/addbrick/fastlane/commits{/sha}',
                                  'git_commits_url': 'https://api.github.com/repos/addbrick/fastlane/git/commits{/sha}',
                                  'comments_url': 'https://api.github.com/repos/addbrick/fastlane/comments{/number}',
                                  'issue_comment_url': 'https://api.github.com/repos/addbrick/fastlane/issues/comments{/number}',
                                  'contents_url': 'https://api.github.com/repos/addbrick/fastlane/contents/{+path}',
                                  'compare_url': 'https://api.github.com/repos/addbrick/fastlane/compare/{base}...{head}',
                                  'merges_url': 'https://api.github.com/repos/addbrick/fastlane/merges',
                                  'archive_url': 'https://api.github.com/repos/addbrick/fastlane/{archive_format}{/ref}',
                                  'downloads_url': 'https://api.github.com/repos/addbrick/fastlane/downloads',
                                  'issues_url': 'https://api.github.com/repos/addbrick/fastlane/issues{/number}',
                                  'pulls_url': 'https://api.github.com/repos/addbrick/fastlane/pulls{/number}',
                                  'milestones_url': 'https://api.github.com/repos/addbrick/fastlane/milestones{/number}',
                                  'notifications_url': 'https://api.github.com/repos/addbrick/fastlane/notifications{?since,all,participating}',
                                  'labels_url': 'https://api.github.com/repos/addbrick/fastlane/labels{/name}',
                                  'releases_url': 'https://api.github.com/repos/addbrick/fastlane/releases{/id}',
                                  'deployments_url': 'https://api.github.com/repos/addbrick/fastlane/deployments',
                                  'created_at': '2017-08-23T23:09:04Z', 'updated_at': '2020-07-09T03:55:28Z',
                                  'pushed_at': '2020-07-09T04:51:05Z',
                                  'git_url': 'git://github.com/addbrick/fastlane.git',
                                  'ssh_url': 'git@github.com:addbrick/fastlane.git',
                                  'clone_url': 'https://github.com/addbrick/fastlane.git',
                                  'svn_url': 'https://github.com/addbrick/fastlane',
                                  'homepage': 'https://fastlane.tools',
                                  'size': 67663, 'stargazers_count': 0, 'watchers_count': 0, 'language': 'Ruby',
                                  'has_issues': False, 'has_projects': True, 'has_downloads': True, 'has_wiki': False,
                                  'has_pages': False, 'forks_count': 0, 'mirror_url': None, 'archived': False,
                                  'disabled': False, 'open_issues_count': 0,
                                  'license': {'key': 'mit', 'name': 'MIT License', 'spdx_id': 'MIT',
                                              'url': 'https://api.github.com/licenses/mit',
                                              'node_id': 'MDc6TGljZW5zZTEz'},
                                  'forks': 0, 'open_issues': 0, 'watchers': 0, 'default_branch': 'master'}},
                'base': {'label': 'fastlane:master', 'ref': 'master', 'sha': '539f562bcbb319e01ce009ba6fc2f36f35ae0415',
                         'user': {'login': 'fastlane', 'id': 11098337, 'node_id': 'MDEyOk9yZ2FuaXphdGlvbjExMDk4MzM3',
                                  'avatar_url': 'https://avatars2.githubusercontent.com/u/11098337?v=4',
                                  'gravatar_id': '',
                                  'url': 'https://api.github.com/users/fastlane',
                                  'html_url': 'https://github.com/fastlane',
                                  'followers_url': 'https://api.github.com/users/fastlane/followers',
                                  'following_url': 'https://api.github.com/users/fastlane/following{/other_user}',
                                  'gists_url': 'https://api.github.com/users/fastlane/gists{/gist_id}',
                                  'starred_url': 'https://api.github.com/users/fastlane/starred{/owner}{/repo}',
                                  'subscriptions_url': 'https://api.github.com/users/fastlane/subscriptions',
                                  'organizations_url': 'https://api.github.com/users/fastlane/orgs',
                                  'repos_url': 'https://api.github.com/users/fastlane/repos',
                                  'events_url': 'https://api.github.com/users/fastlane/events{/privacy}',
                                  'received_events_url': 'https://api.github.com/users/fastlane/received_events',
                                  'type': 'Organization', 'site_admin': False},
                         'repo': {'id': 27442967, 'node_id': 'MDEwOlJlcG9zaXRvcnkyNzQ0Mjk2Nw==', 'name': 'fastlane',
                                  'full_name': 'fastlane/fastlane', 'private': False,
                                  'owner': {'login': 'fastlane', 'id': 11098337,
                                            'node_id': 'MDEyOk9yZ2FuaXphdGlvbjExMDk4MzM3',
                                            'avatar_url': 'https://avatars2.githubusercontent.com/u/11098337?v=4',
                                            'gravatar_id': '', 'url': 'https://api.github.com/users/fastlane',
                                            'html_url': 'https://github.com/fastlane',
                                            'followers_url': 'https://api.github.com/users/fastlane/followers',
                                            'following_url': 'https://api.github.com/users/fastlane/following{/other_user}',
                                            'gists_url': 'https://api.github.com/users/fastlane/gists{/gist_id}',
                                            'starred_url': 'https://api.github.com/users/fastlane/starred{/owner}{/repo}',
                                            'subscriptions_url': 'https://api.github.com/users/fastlane/subscriptions',
                                            'organizations_url': 'https://api.github.com/users/fastlane/orgs',
                                            'repos_url': 'https://api.github.com/users/fastlane/repos',
                                            'events_url': 'https://api.github.com/users/fastlane/events{/privacy}',
                                            'received_events_url': 'https://api.github.com/users/fastlane/received_events',
                                            'type': 'Organization', 'site_admin': False},
                                  'html_url': 'https://github.com/fastlane/fastlane',
                                  'description': '🚀 The easiest way to automate building and releasing your iOS and Android apps',
                                  'fork': False, 'url': 'https://api.github.com/repos/fastlane/fastlane',
                                  'forks_url': 'https://api.github.com/repos/fastlane/fastlane/forks',
                                  'keys_url': 'https://api.github.com/repos/fastlane/fastlane/keys{/key_id}',
                                  'collaborators_url': 'https://api.github.com/repos/fastlane/fastlane/collaborators{/collaborator}',
                                  'teams_url': 'https://api.github.com/repos/fastlane/fastlane/teams',
                                  'hooks_url': 'https://api.github.com/repos/fastlane/fastlane/hooks',
                                  'issue_events_url': 'https://api.github.com/repos/fastlane/fastlane/issues/events{/number}',
                                  'events_url': 'https://api.github.com/repos/fastlane/fastlane/events',
                                  'assignees_url': 'https://api.github.com/repos/fastlane/fastlane/assignees{/user}',
                                  'branches_url': 'https://api.github.com/repos/fastlane/fastlane/branches{/branch}',
                                  'tags_url': 'https://api.github.com/repos/fastlane/fastlane/tags',
                                  'blobs_url': 'https://api.github.com/repos/fastlane/fastlane/git/blobs{/sha}',
                                  'git_tags_url': 'https://api.github.com/repos/fastlane/fastlane/git/tags{/sha}',
                                  'git_refs_url': 'https://api.github.com/repos/fastlane/fastlane/git/refs{/sha}',
                                  'trees_url': 'https://api.github.com/repos/fastlane/fastlane/git/trees{/sha}',
                                  'statuses_url': 'https://api.github.com/repos/fastlane/fastlane/statuses/{sha}',
                                  'languages_url': 'https://api.github.com/repos/fastlane/fastlane/languages',
                                  'stargazers_url': 'https://api.github.com/repos/fastlane/fastlane/stargazers',
                                  'contributors_url': 'https://api.github.com/repos/fastlane/fastlane/contributors',
                                  'subscribers_url': 'https://api.github.com/repos/fastlane/fastlane/subscribers',
                                  'subscription_url': 'https://api.github.com/repos/fastlane/fastlane/subscription',
                                  'commits_url': 'https://api.github.com/repos/fastlane/fastlane/commits{/sha}',
                                  'git_commits_url': 'https://api.github.com/repos/fastlane/fastlane/git/commits{/sha}',
                                  'comments_url': 'https://api.github.com/repos/fastlane/fastlane/comments{/number}',
                                  'issue_comment_url': 'https://api.github.com/repos/fastlane/fastlane/issues/comments{/number}',
                                  'contents_url': 'https://api.github.com/repos/fastlane/fastlane/contents/{+path}',
                                  'compare_url': 'https://api.github.com/repos/fastlane/fastlane/compare/{base}...{head}',
                                  'merges_url': 'https://api.github.com/repos/fastlane/fastlane/merges',
                                  'archive_url': 'https://api.github.com/repos/fastlane/fastlane/{archive_format}{/ref}',
                                  'downloads_url': 'https://api.github.com/repos/fastlane/fastlane/downloads',
                                  'issues_url': 'https://api.github.com/repos/fastlane/fastlane/issues{/number}',
                                  'pulls_url': 'https://api.github.com/repos/fastlane/fastlane/pulls{/number}',
                                  'milestones_url': 'https://api.github.com/repos/fastlane/fastlane/milestones{/number}',
                                  'notifications_url': 'https://api.github.com/repos/fastlane/fastlane/notifications{?since,all,participating}',
                                  'labels_url': 'https://api.github.com/repos/fastlane/fastlane/labels{/name}',
                                  'releases_url': 'https://api.github.com/repos/fastlane/fastlane/releases{/id}',
                                  'deployments_url': 'https://api.github.com/repos/fastlane/fastlane/deployments',
                                  'created_at': '2014-12-02T17:00:38Z', 'updated_at': '2020-07-09T08:37:20Z',
                                  'pushed_at': '2020-07-09T04:54:16Z',
                                  'git_url': 'git://github.com/fastlane/fastlane.git',
                                  'ssh_url': 'git@github.com:fastlane/fastlane.git',
                                  'clone_url': 'https://github.com/fastlane/fastlane.git',
                                  'svn_url': 'https://github.com/fastlane/fastlane',
                                  'homepage': 'https://fastlane.tools',
                                  'size': 68702, 'stargazers_count': 29252, 'watchers_count': 29252, 'language': 'Ruby',
                                  'has_issues': True, 'has_projects': True, 'has_downloads': True, 'has_wiki': False,
                                  'has_pages': False, 'forks_count': 4593, 'mirror_url': None, 'archived': False,
                                  'disabled': False, 'open_issues_count': 222,
                                  'license': {'key': 'mit', 'name': 'MIT License', 'spdx_id': 'MIT',
                                              'url': 'https://api.github.com/licenses/mit',
                                              'node_id': 'MDc6TGljZW5zZTEz'},
                                  'forks': 4593, 'open_issues': 222, 'watchers': 29252, 'default_branch': 'master'}},
                '_links': {'self': {'href': 'https://api.github.com/repos/fastlane/fastlane/pulls/16808'},
                           'html': {'href': 'https://github.com/fastlane/fastlane/pull/16808'},
                           'issue': {'href': 'https://api.github.com/repos/fastlane/fastlane/issues/16808'},
                           'comments': {'href': 'https://api.github.com/repos/fastlane/fastlane/issues/16808/comments'},
                           'review_comments': {
                               'href': 'https://api.github.com/repos/fastlane/fastlane/pulls/16808/comments'},
                           'review_comment': {
                               'href': 'https://api.github.com/repos/fastlane/fastlane/pulls/comments{/number}'},
                           'commits': {'href': 'https://api.github.com/repos/fastlane/fastlane/pulls/16808/commits'},
                           'statuses': {
                               'href': 'https://api.github.com/repos/fastlane/fastlane/statuses/898998357e4e9953a0e800efda03f6debbee9ee9'}},
                'author_association': 'CONTRIBUTOR', 'active_lock_reason': None},
            {
                'number': 16809,
                'state': 'open',
                'created_at':   (date + datetime.timedelta(days=-1)).strftime(DATETIME_FORMAT),
            },
            {
                'number': 16810,
                'state': 'open',
                'created_at': (date + datetime.timedelta(days=-60)).strftime(DATETIME_FORMAT),
            },
            {
                'number': 16811,
                'state': 'open',
                'created_at': (date + datetime.timedelta(days=-60)).strftime(DATETIME_FORMAT),
            },
            {
                'number': 16812,
                'state': 'closed',
                'created_at': (date + datetime.timedelta(days=-2)).strftime(DATETIME_FORMAT),
            },
        ]
        raw_issues = [
            {  # open, not old
                'url': 'https://api.github.com/repos/fastlane/fastlane/issues/16808',
                'repository_url': 'https://api.github.com/repos/fastlane/fastlane',
                'labels_url': 'https://api.github.com/repos/fastlane/fastlane/issues/16808/labels{/name}',
                'comments_url': 'https://api.github.com/repos/fastlane/fastlane/issues/16808/comments',
                'events_url': 'https://api.github.com/repos/fastlane/fastlane/issues/16808/events',
                'html_url': 'https://github.com/fastlane/fastlane/pull/16808', 'id': 653762371,
                'node_id': 'MDExOlB1bGxSZXF1ZXN0NDQ2NjE2NDYw', 'number': 16808,
                'title': 'add shortcuts for getting current pending release and current in revi…',
                'user': {'login': 'addbrick', 'id': 800916, 'node_id': 'MDQ6VXNlcjgwMDkxNg==',
                         'avatar_url': 'https://avatars1.githubusercontent.com/u/800916?v=4', 'gravatar_id': '',
                         'url': 'https://api.github.com/users/addbrick', 'html_url': 'https://github.com/addbrick',
                         'followers_url': 'https://api.github.com/users/addbrick/followers',
                         'following_url': 'https://api.github.com/users/addbrick/following{/other_user}',
                         'gists_url': 'https://api.github.com/users/addbrick/gists{/gist_id}',
                         'starred_url': 'https://api.github.com/users/addbrick/starred{/owner}{/repo}',
                         'subscriptions_url': 'https://api.github.com/users/addbrick/subscriptions',
                         'organizations_url': 'https://api.github.com/users/addbrick/orgs',
                         'repos_url': 'https://api.github.com/users/addbrick/repos',
                         'events_url': 'https://api.github.com/users/addbrick/events{/privacy}',
                         'received_events_url': 'https://api.github.com/users/addbrick/received_events', 'type': 'User',
                         'site_admin': False}, 'labels': [{'id': 560540952, 'node_id': 'MDU6TGFiZWw1NjA1NDA5NTI=',
                                                           'url': 'https://api.github.com/repos/fastlane/fastlane/labels/cla:%20yes',
                                                           'name': 'cla: yes', 'color': '0e8a16', 'default': False,
                                                           'description': None}], 'state': 'open', 'locked': False,
                'assignee': None, 'assignees': [], 'milestone': None, 'comments': 0,
                'created_at': (date + datetime.timedelta(days=-1)).strftime(DATETIME_FORMAT),
                'updated_at': '2020-07-09T04:54:19Z', 'closed_at': None, 'author_association': 'CONTRIBUTOR',
                'active_lock_reason': None,
                'pull_request': {'url': 'https://api.github.com/repos/fastlane/fastlane/pulls/16808',
                                 'html_url': 'https://github.com/fastlane/fastlane/pull/16808',
                                 'diff_url': 'https://github.com/fastlane/fastlane/pull/16808.diff',
                                 'patch_url': 'https://github.com/fastlane/fastlane/pull/16808.patch'},
                'body': "…ew app store version\r\n\r\n<!-- Thanks for contributing to _fastlane_! Before you submit your pull request, please make sure to check the following boxes by putting an x in the [ ] (don't: [x ], [ x], do: [x]) -->\r\n\r\n### Checklist\r\n- [X] I've run `bundle exec rspec` from the root directory to see all new and existing tests pass\r\n- [X] I've followed the _fastlane_ code style and run `bundle exec rubocop -a` to ensure the code style is valid\r\n- [X] I've read the [Contribution Guidelines](https://github.com/fastlane/fastlane/blob/master/CONTRIBUTING.md)\r\n- [X] I've updated the documentation if necessary.\r\n\r\n### Motivation and Context\r\n<!-- Why is this change required? What problem does it solve? -->\r\nThis adds short cuts for getting the app store version which is In Review via `get_in_review_app_store_version`, and Pending Developer Release via `get_pending_release_app_store_version`. This way I don't have to remember the filters when looking these versions up.\r\n<!-- If it fixes an open issue, please link to the issue here. -->\r\n\r\n### Description\r\n<!-- Describe your changes in detail. -->\r\nThis adds short cuts for getting the app store version which is In Review via `get_in_review_app_store_version`, and Pending Developer Release via `get_pending_release_app_store_version`.\r\n<!-- Please describe in detail how you tested your changes. -->\r\n\r\n### Testing Steps\r\n<!-- Optional: steps, commands, or code used to test your changes. -->\r\n<!-- Providing these will reduce the time needed for testing and review by the fastlane team. -->\r\n"
            },
            {  # open, not old
                'number': 16809,
                'state': 'open',
                'created_at': (date + datetime.timedelta(days=-2)).strftime(DATETIME_FORMAT),
                'closed_at': None,
            },
            {  # open, not old
                'number': 16810,
                'state': 'open',
                'created_at': (date + datetime.timedelta(days=-3)).strftime(DATETIME_FORMAT),
                'closed_at': None,
            },
            {  # open, old
                'number': 16811,
                'state': 'open',
                'created_at': (date + datetime.timedelta(days=-17)).strftime(DATETIME_FORMAT),
                'closed_at': None,
            },
            {  # closed, old
                'number': 16812,
                'state': 'closed',
                'created_at': (date + datetime.timedelta(days=-20)).strftime(DATETIME_FORMAT),
                'closed_at': (date + datetime.timedelta(days=-2)).strftime(DATETIME_FORMAT),
            },
            {  # closed, not old
                'number': 16813,
                'state': 'closed',
                'created_at': (date + datetime.timedelta(days=-20)).strftime(DATETIME_FORMAT),
                'closed_at': (date + datetime.timedelta(days=-10)).strftime(DATETIME_FORMAT),
            },
            {  # closed, not old
                'number': 16814,
                'state': 'closed',
                'created_at': (date + datetime.timedelta(days=-18)).strftime(DATETIME_FORMAT),
                'closed_at': (date + datetime.timedelta(days=-16)).strftime(DATETIME_FORMAT),
            },
        ]

        self.repo.commits = [Commit(raw_commit) for raw_commit in raw_commits]
        self.repo.pulls = [Pull(raw_pull) for raw_pull in raw_pulls]
        self.repo.issues = [Issue(raw_issue) for raw_issue in raw_issues]


class TestCommit(TestRepository):
    def test_commit_authors_count(self):
        """Тест количества позиций"""
        top_authors = self.repo.commit_authors()
        self.assertEqual(len(top_authors), 2)

    def test_commit_authors_first(self):
        """Тест первой позиции"""
        top_authors = self.repo.commit_authors()
        self.assertEqual(top_authors[0], ('joshdholtz', 2))

    def test_commit_authors_second(self):
        """Тест второй позиции"""
        top_authors = self.repo.commit_authors()
        self.assertEqual(top_authors[1], ('CognitiveDisson', 1))


class TestPull(TestRepository):
    def test_open_pull(self):
        counted_open_pulls = self.repo.count_open(self.repo.pulls)
        self.assertEqual(counted_open_pulls, 4)

    def test_closed_pull(self):
        counted_closed_pulls = self.repo.count_closed(self.repo.pulls)
        self.assertEqual(counted_closed_pulls, 1)

    def test_old_pull(self):
        counted_old_pulls = self.repo.count_old(self.repo.pulls)
        self.assertEqual(counted_old_pulls, 2)


class TestIssue(TestRepository):
    def test_open_issue(self):
        counted_open_issues = self.repo.count_open(self.repo.issues)
        self.assertEqual(counted_open_issues, 4)

    def test_closed_issue(self):
        counted_closed_issues = self.repo.count_closed(self.repo.issues)
        self.assertEqual(counted_closed_issues, 3)

    def test_old_issue(self):
        counted_old_issues = self.repo.count_old(self.repo.issues)
        self.assertEqual(counted_old_issues, 2)
