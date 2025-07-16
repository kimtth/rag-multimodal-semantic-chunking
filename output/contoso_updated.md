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


<figure>### FigureContent 

 "The image presents a rectangular graphic enclosed in a black border. Inside this rectangle, there is a visual element on the left side—a stylized representation of a paper sheet, slightly angled to suggest it is either being turned or has a folded corner. This graphic is depicted in a simple gray-scale style with a minimalistic yet recognizable design, emphasizing the paper's shape and folding corner.

Adjacent to the paper graphic, the text reads "Article version of this poster" in a bold, blue font. The choice of blue adds a sense of clarity and a welcoming contrast against the otherwise monochrome graphic. The font style is straightforward and professional, likely intended to convey the information clearly and quickly to the reader.

Overall, this image serves as a button or indicator to access an article that corresponds to the content of a poster, suggesting it is part of a digital platform or a part of a presentation where viewers can access written content related to an illustrated poster. The combination of the visual metaphor of a page with the textual information effectively communicates its intended purpose."</figure>


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


<figure>### FigureContent 

 "The image is a world map showcasing various locations that are categorized into three types of operational centers: Headquarters, Regional Hubs, and Satellites. These categories are visually distinguished by color-coded labels and a legend located in the lower left corner of the image.

### Key Elements:

1. **Color Coding**:
   - **Headquarters**: Represented by green, with "Paris" highlighted prominently.
   - **Regional Hub**: Shown in dark gray, with several major cities designated under this label, such as New York, Munich, and Dubai.
   - **Satellite**: Depicted in light blue, indicating additional locations that serve as satellite offices. 

2. **Geographical Distribution**:
   - The image highlights major cities across North America, Europe, Asia, and South America, displaying a global reach:
     - **North America**: Examples include Los Angeles, Chicago, New York, and Toronto.
     - **Europe**: Key cities include London, Paris, Munich, and Milan.
     - **Asia**: Important locations shown include Tokyo, Beijing, Mumbai, and Singapore.
     - **South America**: Sao Paulo is marked as a satellite location.

3. **Connections**:
   - Several lines connect cities, suggesting a network among these operational centers. The lines vary in style, with some being solid and others dotted, indicating different types of connections or relationships between locations.

4. **Text Labels**:
   - Each city is labeled clearly with its name. The font is consistent across the map, ensuring readability.
   - Labels for the headquarters, regional hubs, and satellites convey their significance, with headquarters in green being particularly emphasized.
   
5. **Background**:
   - The map is set against a light gray background, which allows the labeled cities and their color coding to stand out. 

### Summary:
Overall, the image serves as a comprehensive overview of a company's global operational structure, illustrating the hierarchy and geographical spread of its offices. The use of color coding aids in quickly identifying the nature of each office, while the connected lines emphasize the interrelations between these different locations across the globe."</figure>


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


<figure>### FigureContent 

 "The image presented is a structured overview of the organizational framework of the Contoso Corporation, detailing three distinct types of office locations: Headquarters, Regional Hubs, and Satellite Offices. Each section is color-coded for clarity, with the headquarters represented in green, regional hubs in gray, and satellite offices in blue.

1. **Headquarters**:
   - The section is highlighted in green and labeled "Headquarters" in bold, large white font.
   - A description follows, stating that the Contoso Corporation headquarters is a large corporate campus located on the outskirts of Paris. It mentions the presence of numerous buildings dedicated to administrative, engineering, and manufacturing activities.
   - The headquarters houses all of Contoso's data centers and internet operations.
   - There is a key statistic indicating that the headquarters employs **15,000 workers**.

2. **Regional Hubs**:
   - This section is visually distinguished by a gray background, with the title "Regional hubs" prominently displayed in bold white font.
   - The description explains that regional hub offices are dedicated to serving specific global regions, employing 60% sales and support staff.
   - It notes that each hub is connected to the Paris headquarters via a high-bandwidth WAN link.
   - The average workforce at each regional hub is stated to be **2,000 workers**.

3. **Satellite Offices**:
   - Displayed with a blue background, this section is titled "Satellite offices" in bold, white font.
   - The description indicates that satellite offices comprise 80% sales and support staff and aim to maintain a physical presence for Contoso customers in major cities and suburban areas.
   - Similar to regional hubs, each satellite office connects to a regional hub with a high-bandwidth WAN link.
   - An average of **250 workers** is noted for each satellite office.

4. **Mobile Workforce Insight**:
   - At the bottom of the figure, there is a statistic in a separate text box indicating that **25% of Contoso's workforce is mobile-only**, with a higher prevalence in the regional hubs and satellite offices.
   - The text emphasizes that providing enhanced support for these mobile-only workers is a critical business goal for Contoso.

Overall, the image presents a clear, organized depiction of Contoso's operational structure alongside relevant workforce statistics, emphasizing the scale and connectivity of its various office locations."</figure>


### Security

Security for cloud-based identities and
data must include data protection,
administrative privilege management,
threat awareness, and the
implementation of data governance and
security policies.


<figure>### FigureContent 

 "The image features a clean and modern design focused on the theme of cloud computing and enterprise architecture.

**Key elements in the image:**

1. **Title/Text:**
   - The prominent text reads "Microsoft Cloud Networking for Enterprise Architects." 
   - The font is clear and professional, likely aimed at a corporate or technical audience. The color of the text is a shade of blue, which is often associated with trust and technology.

2. **Iconography:**
   - To the left of the text, there is a graphical representation that combines elements of cloud computing and networking.
   - The cloud is depicted in a stylized manner, containing a simple shape that resembles a cloud outline.
   - Within the cloud, there is an abstract representation of a network or device, possibly symbolizing servers or connections related to cloud services. This aspect highlights the topic of cloud networking.

3. **Layout:**
   - The image maintains a horizontal format, with the icon positioned to the left and the text aligned to the right. This layout is effective for readability and creates a balanced visual effect.
   - The use of negative space around the elements contributes to a clean and sophisticated look.

4. **Color Scheme:**
   - The predominant colors are shades of blue (for the text) and gray (for the icon), which convey a professional and technical tone.

Overall, the image serves as a header or main title in a document, likely indicating a section focused on Microsoft’s cloud networking solutions specifically tailored for enterprise-level architects. The clear iconography and modern design suggest an emphasis on contemporary technology and its applications in large-scale enterprise environments."</figure>


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


<figure>### FigureContent 

 "The image features a titled section that prominently reads "Microsoft Cloud Identity for Enterprise Architects." The text is styled in a bold, modern font with a blue color that stands out against the lighter background, suggesting a professional and contemporary design.

To the left of the text, there is an illustrative graphic that comprises a cloud shape, symbolizing cloud computing or cloud services. Below the cloud, there is an icon representing a person, which conveys the concept of user identity management within cloud services. Alongside, there is a small triangle shape, which could imply a directional or informational component. This combination of graphics is likely intended to visually reinforce the theme of identity and cloud services in relation to enterprise architecture.

Overall, the combination of elements—the cloud, the person icon, and the title—suggests a focus on the integration of identity management solutions that Microsoft offers for enterprise-level IT professionals. The design elements indicate a clean and modern approach, likely aiming to appeal to an audience of enterprise architects or IT decision-makers."</figure>


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


<figure>### FigureContent 

 "The image appears to be a title or header graphic related to the topic of "Microsoft Cloud Security for Enterprise Architects." 

### Key Elements:

1. **Text Content**: 
   - The primary text is "Microsoft Cloud Security for Enterprise Architects," which suggests that the content is aimed at enterprise architects involved in cloud security practices or solutions. The usage of “Microsoft” indicates the focus on its cloud security offerings.

2. **Font and Color**:
   - The text is displayed in a bold, modern sans-serif font, enhancing readability and giving a professional appearance. The color of the text is a vibrant blue, which is visually appealing and in line with Microsoft's branding.

3. **Imagery and Icons**:
   - To the left of the text, there are two icons:
     - **Cloud Icon**: Represented as a stylized cloud outline, this suggests the context of cloud computing and indicates the subject of the security practices being discussed.
     - **Lock Icon**: There is a padlock symbol incorporated into the design, which commonly represents security and emphasizes the focus on safeguarding data and services in the cloud.
     - **Triangle Symbol**: There’s a small triangular shape which seems to be a design element, likely implying a technical or architectural aspect closely related to enterprise systems.

### Layout:
- The icons are positioned to the left of the text, creating a cohesive visual structure where the imagery complements the title text. The arrangement is horizontal, making the information accessible and easy to associate the icons with the text.

### Overall Impression:
The graphic is clean and professional, designed to attract the attention of enterprise architects who are interested in or responsible for implementing security protocols in Microsoft’s cloud environment. The combination of text and imagery ideally communicates the core subject of cloud security in a straightforward manner."</figure>


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


<figure>### FigureContent 

 "The image depicts the logo of Microsoft, which consists of both a colored icon and the company name.

1. **Icon Elements**:
   - The icon is located on the left side of the logo and consists of four colored squares arranged in a 2x2 grid.
   - The top left square is colored red. 
   - The top right square is green. 
   - The bottom left square is blue. 
   - The bottom right square is yellow. 
   - The squares are designed to evoke a sense of a window or grid, reflecting the company’s roots in software development, particularly in operating systems.

2. **Text Elements**:
   - Next to the icon is the text "Microsoft" in a bold, sans-serif font.
   - The text is colored in a medium gray tone, which provides a modern and professional aesthetic. 
   - The letters are all uppercase, except for the second letter 'i,' which is lowercase.
   - The font style is clean and straightforward, enhancing legibility and familiarity.

3. **Overall Appearance**:
   - The overall look of the logo is contemporary, reflecting Microsoft's brand identity as a leading technology company.
   - The combination of vibrant colors in the icon coupled with the neutral color of the text creates a balanced and eye-catching design.
   - The logo is likely presented on a white or light background, which helps the colors stand out more prominently.

This logo effectively conveys Microsoft’s identity as an innovative and accessible technology provider, maintaining a balance between professionalism and vibrancy."</figure>


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
