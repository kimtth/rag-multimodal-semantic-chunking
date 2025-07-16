# Contoso in the Microsoft Cloud

How a fictional but representative global
organization has implemented the
Microsoft Cloud

This topic is 1 of 7 in a series
1

2

3

4

5

6

7


## The Contoso Corporation

The Contoso Corporation is a global business with headquarters in Paris, France. It is a
conglomerate manufacturing, sales, and support organization with over 100,000 products.


<figure>

Article version
of this poster

</figure>


### Contoso's worldwide organization


<figure>
<figcaption>Contoso's offices around the world follow a three tier design.</figcaption>

Toronto

Edinburgh

Novosibirsk

Detroit

Montreal

Cologne

Chicago

Boston

Minneapolis

Tokyo

Moscow

Dublin

Beijing

Silicon Valley

Thames Valley

Munich

Los Angeles

St. Louis

New York

Paris

Irvine

Philadelphia

Dubai

Mumbai

Dallas

Reston

Milan

Charlotte

Taipei

Tel Aviv

Atlanta

Guangzhou

Mexico City

Houston

Bangalore

Headquarters

Sao Paulo

Singapore

Regional Hub

Satellite

Johannesburg

</figure>


### Headquarters


### Regional hubs


### Satellite offices

The Contoso Corporation
headquarters is a large corporate
campus on the outskirts of Paris
with dozens of buildings for
administrative, engineering, and
manufacturing facilities. All of
Contoso's datacenters and it's
Internet presence are housed in the
Paris head quarters.

Regional hub offices serve a specific
region of the world with 60% sales
and support staff. Each regional hub
is connected to the Paris
headquarters with a high-bandwidth
WAN link.

Satellite offices contain 80% sales and
support staff and provide a physical
and on-site presence for Contoso
customers in key cities or sub-
regions. Each satellite office is
connected to a regional hub with a
high-bandwidth WAN link.

25% of Contoso's
workforce is mobile-
only, with a higher
percentage of
mobile-only workers
in the regional hubs
and satellite offices.

Providing better
support for mobile-
only workers is an
important business
goal for Contoso.

Each regional hub has an average of
2,000 workers.

The headquarters has 15,000
workers.

Each satellite office has an average of
250 workers.


## Elements of Contoso's implementation of the Microsoft cloud

Contoso's IT architects have identified the following elements when planning for the adoption of Microsoft's cloud offerings.


### Networking

Networking includes the connectivity to
Microsoft's cloud offerings and enough
bandwidth to be performant under peak
loads. Some connectivity will be over
local Internet connections and some will
be across Contoso's private network
infrastructure.


<figure>

Microsoft Cloud Networking
for Enterprise Architects

</figure>


### Identity

Contoso uses a Windows Server AD forest
for its internal identity provider and also
federates with third-party providers for
customer and partners. Contoso must
leverage the internal set of accounts for
Microsoft's cloud offerings. Access to
cloud-based apps for customers and
partners must leverage third-party
identity providers as well.


<figure>

Microsoft Cloud Identity for
Enterprise Architects

</figure>


### Security

Security for cloud-based identities and
data must include data protection,
administrative privilege management,
threat awareness, and the
implementation of data governance and
security policies.


<figure>

Microsoft Cloud Security for
Enterprise Architects

</figure>


### Management

Management for cloud-based apps and
SaaS workloads will need the ability to
maintain settings, data, accounts, policies,
and permissions and to monitor ongoing
health and performance. Existing server
management tools will be used to
manage virtual machines in Azure laaS.

September 2017

<!-- PageFooter="@ 2016 Microsoft Corporation. All rights reserved. To send feedback about this documentation, please write to us at CloudAdopt@microsoft.com." -->


<figure>

Microsoft

</figure>


<!-- PageBreak -->


## Contoso in the Microsoft Cloud

How a fictional but representative global
organization has implemented the
Microsoft Cloud

This topic is 2 of 7 in a series
1
2

3

4

5

6

7


### Contoso's IT infrastructure and needs

Contoso is in the process of transitioning from an on-premises, centralized IT infrastructure to a cloud-inclusive
one that incorporates cloud-based personal productivity workloads, applications, and hybrid scenarios.


#### Contoso's existing IT infrastructure

Contoso uses a mostly centralized on-premises IT infrastructure, with application datacenters in the
Paris headquarters.


<figure>

Headquarters

DMZ

Internet

Application
datacenters

Remote access/
proxy

Remote and
mobile-only
workers

Public web site

On-premises
workers

Partner extranet

Internal firewall

External firewall

</figure>


In Contoso's DMZ, different sets of servers
provide:

. Remote access to the Contoso intranet
and web proxying for workers in the
Paris headquarters.

· Hosting for the Contoso public web site,
from which customers can order
products, parts, or supplies.

· Hosting for the Contoso partner
extranet for partner communication and
collaboration.


### Contoso's business needs


#### 1 Adhere to regional regulatory requirements

To prevent fines and maintain good relations
with local governments, Contoso must ensure
compliance with data storage and encryption
regulations.


#### 4 Reduce remote access infrastructure

By moving resources commonly accessed
by remote workers to the cloud, Contoso
will save money by reducing maintenance
and support costs for their remote access
solution.

2
Improve vendor and partner
management

The partner extranet is aging and expensive
to maintain. Contoso wants to replace it
with a cloud-based solution that uses
federated authentication.


#### 3 Improve mobile workforce productivity, device management, and access

Contoso's mobile-only workforce is
expanding and needs device management to
ensure intellectual property protection and
more efficient access to resources.

5
Scale down on-premises datacenters

The Contoso datacenters contain hundreds
of servers, some of which are running
legacy or archival functions that distract IT
staff from maintaining high business value
workloads.

6
Scale-up computing and storage
resources for end-of-quarter processing

End-of-quarter financial accounting and
projection processing along with inventory
management requires short-term increases
in servers and storage.


### Mapping Contoso's business needs to Microsoft's cloud offerings

SaaS
Software as a Service

Office 365: Primary personal
and group productivity
applications in the cloud.

1

3

5

Dynamics 365: Use cloud-
based customer and vendor
management. Remove
partner extranet in the DMZ.

2

Intune/EMS: Manage iOS
and Android devices.

3


#### Azure PaaS Platform as a Service

Host sales and support
documents and information
systems using cloud-based
apps.

3

Mobile applications are
cloud-based, rather than
Paris datacenter-based.

3

4


#### Azure IaaS Infrastructure as a Service

Move archival and legacy
systems to cloud-based servers.

5

Migrate low-use apps and data
out of on-premises datacenters.

5

Add temporary servers and
storage for end-of-quarter
processing needs.

6

<!-- PageFooter="September 2017" -->
<!-- PageFooter="@ 2016 Microsoft Corporation. All rights reserved. To send feedback about this documentation, please write to us at CloudAdopt@microsoft.com." -->


<figure>

Microsoft

</figure>


<!-- PageBreak -->


### Contoso in the Microsoft Cloud

How a fictional but representative global
organization has implemented the
Microsoft Cloud

This topic is 6 of 7 in a series
1

2

3

4

5

6
7


#### Security

Contoso is serious about their information security and protection. When transitioning their IT
infrastructure to a cloud-inclusive one, they made sure that their on-premises security requirements
were supported and implemented in Microsoft's cloud offerings.


#### Contoso's security requirements in the cloud


<table>
<tr>
<td>Strong authentication to cloud resources</td>
<td>Cloud resource access must be authenticated and, where possible, leverage multi-factor authentication.</td>
</tr>
<tr>
<td>Encryption for traffic across the Internet</td>
<td>No data sent across the Internet is in plain text form. Always use HTTPS connections, IPsec, or other end -to-end data encryption methods.</td>
</tr>
<tr>
<td>Encryption for data at rest in the cloud</td>
<td>All data stored on disks or elsewhere in the cloud must be in an encrypted form.</td>
</tr>
<tr>
<td>ACLs for least privilege access</td>
<td>Account permissions to access resources in the cloud and what they are allowed to do must follow least-privilege guidelines.</td>
</tr>
</table>


#### Contoso's data sensitivity classification

Using the information in Microsoft's Data Classification Toolkit, Contoso performed an analysis of their data and determined the
following levels.


<table>
<tr>
<th>Level 1: Low business value</th>
<th>Level 2: Medium business value</th>
<th>Level 3: High business value</th>
</tr>
<tr>
<td>Data is encrypted and available only to authenticated users</td>
<td>Level 1 plus strong authentication and data loss protection</td>
<td>Level 2 plus the highest levels of encryption, authentication, and auditing</td>
</tr>
<tr>
<td>Provided for all data stored on premises and in cloud- based storage and workloads, such as Office 365. Data is encrypted while it resides in the service and in transit between the service and client devices.</td>
<td>Strong authentication includes multi-factor authentication with SMS validation. Data loss prevention ensures that sensitive or critical information does not travel outside the on-premises network.</td>
<td>The highest levels of encryption for data at rest and in the cloud, compliant with regional regulations, combined with multi-factor authentication with smart cards and granular auditing and alerting.</td>
</tr>
<tr>
<td>Examples of Level 1 data are normal business communications (email) and files for administrative, sales, and support workers.</td>
<td>Examples of Level 2 data are financial and legal information and research and development data for new products.</td>
<td>Examples of Level 3 data are customer and partner personally identifiable information and product engineering specifications and proprietary manufacturing techniques.</td>
</tr>
</table>


##### Data classification toolkit


#### Mapping Microsoft cloud offerings and features to Contoso's data levels


<table>
<tr>
<th></th>
<th>SaaS</th>
<th>Azure PaaS</th>
<th>Azure IaaS</th>
</tr>
<tr>
<td>Level 1: Low business value</td>
<td>. HTTPS for all connections · Encryption at rest</td>
<td>. Support only HTTPS connections · Encrypt files stored in Azure</td>
<td>· Require HTTPS or IPsec for server access · Azure disk encryption</td>
</tr>
<tr>
<td>Level 2: Medium business value</td>
<td>· Azure AD multi-factor authentication (MFA) with SMS</td>
<td>· Use Azure Key Vault for encryption keys · Azure AD MFA with SMS</td>
<td>· MFA with SMS</td>
</tr>
<tr>
<td>Level 3: High business value</td>
<td>. Azure Rights Management System (RMS) . Azure AD MFA with smart cards . Intune conditional access</td>
<td>· Azure RMS · Azure AD MFA with smart cards</td>
<td>. MFA with smart cards</td>
</tr>
</table>


<!-- PageFooter="Continued on next page" -->
