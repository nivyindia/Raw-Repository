# App Script

function createNivyGrowthPartnerForm() {
// ======== 1️⃣ Create Form ========
const form = FormApp.create('NIVY Growth Partner Quick Hire Form')
.setDescription('Apply for NIVY Growth Partner (Part-Time | Remote). This is a part-time, performance-based role. Pocket money income, not a full-time job.');

// SECTION 1: BASIC DETAILS
form.addTextItem().setTitle('Full Name').setRequired(true);
form.addTextItem().setTitle('Email Address').setRequired(true);
form.addTextItem().setTitle('WhatsApp / Telegram Number (with country code)').setRequired(true);
form.addTextItem().setTitle('Country of Residence').setRequired(true);
form.addMultipleChoiceItem()
.setTitle('Age Group')
.setChoices([
form.createChoice('Below 18'),
form.createChoice('18–22'),
form.createChoice('23–30'),
form.createChoice('31–40'),
form.createChoice('40+')
])
.setRequired(true);

// SECTION 2: BACKGROUND
form.addMultipleChoiceItem()
.setTitle('Current Status')
.setChoices([
form.createChoice('Student'),
form.createChoice('Fresher'),
form.createChoice('Working Professional'),
form.createChoice('Sales / BDE Professional'),
form.createChoice('Freelancer / Virtual Assistant'),
form.createChoice('Homemaker'),
form.createChoice('Other')
])
.setRequired(true);

form.addCheckboxItem()
.setTitle('Have you done any of the following before?')
.setChoices([
form.createChoice('Social media posting/commenting'),
form.createChoice('WhatsApp / Email outreach'),
form.createChoice('Referral-based work'),
form.createChoice('Digital marketing basics'),
form.createChoice('Sales / BDE work'),
form.createChoice('None of the above')
]);

// SECTION 3: ROLE UNDERSTANDING
form.addMultipleChoiceItem()
.setTitle('This role is NOT a full-time job and has NO fixed salary. Do you understand this?')
.setChoices([
form.createChoice('Yes, I understand'),
form.createChoice('No')
])
.setRequired(true);

form.addMultipleChoiceItem()
.setTitle('How much time can you realistically give per day?')
.setChoices([
form.createChoice('30 minutes'),
form.createChoice('1 hour'),
form.createChoice('2+ hours')
])
.setRequired(true);

form.addMultipleChoiceItem()
.setTitle('What device will you use for this role?')
.setChoices([
form.createChoice('Mobile only'),
form.createChoice('Laptop only'),
form.createChoice('Both mobile & laptop')
])
.setRequired(true);

// SECTION 4: EARNING EXPECTATION & INTENT
form.addMultipleChoiceItem()
.setTitle('This role offers performance-based pocket-money income (approx. USD 50–150/month). Are you comfortable with this?')
.setChoices([
form.createChoice('Yes'),
form.createChoice('No')
])
.setRequired(true);

form.addParagraphTextItem()
.setTitle('Why are you interested in the Growth Partner role at NIVY?');

// SECTION 5: SKILLS & NETWORK
form.addCheckboxItem()
.setTitle('Which platforms are you active on?')
.setChoices([
form.createChoice('LinkedIn'),
form.createChoice('Facebook'),
form.createChoice('Instagram'),
form.createChoice('WhatsApp / Telegram groups'),
form.createChoice('Email outreach'),
form.createChoice('None')
]);

form.addMultipleChoiceItem()
.setTitle('Do you have access to business owners, professionals, or startup communities?')
.setChoices([
form.createChoice('Yes'),
form.createChoice('No'),
form.createChoice('Not sure')
]);

// SECTION 6: FINAL CONFIRMATION
form.addCheckboxItem()
.setTitle('I confirm that:')
.setChoices([
form.createChoice('This is a part-time, contribution-based role'),
form.createChoice('There is no joining fee'),
form.createChoice('Earnings depend on performance'),
form.createChoice('I am applying genuinely')
])
.setRequired(true);

form.addMultipleChoiceItem()
.setTitle('How did you find this opportunity?')
.setChoices([
form.createChoice('LinkedIn'),
form.createChoice('Instagram'),
form.createChoice('Facebook'),
form.createChoice('WhatsApp / Telegram'),
form.createChoice('Referral'),
form.createChoice('Other')
]);

// SECTION 7: OPTIONAL
form.addTextItem().setTitle('Resume / LinkedIn profile link (optional)');

Logger.log('Form created: ' + form.getEditUrl());

// ======== 2️⃣ Link to Sheet ========
const sheet = SpreadsheetApp.create('NIVY Growth Partner Responses');
form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());
Logger.log('Responses Sheet: ' + sheet.getUrl());
}

// ====== 3️⃣ Auto Email & Scoring Script ======
const MIN_SCORE = 70;
const COMPANY_NAME = "NIVY";
const COMPANY_WEBSITE = "[https://www.thenivy.com](https://www.thenivy.com/)";
const HR_EMAIL = "[careers.nivy@gmail.com](mailto:careers.nivy@gmail.com)";

// Calculate score based on answers
function calculateScore(row) {
let score = 0;

// Background
switch(row["Current Status"]) {
case "Student":
case "Fresher":
case "Homemaker":
case "Other": score += 5; break;
case "Working Professional": score += 10; break;
case "Sales / BDE Professional":
case "Freelancer / Virtual Assistant": score += 15; break;
}

const prevExp = row["Have you done any of the following before?"] ? row["Have you done any of the following before?"].split(",") : [];
prevExp.forEach(exp => {
if(["Social media posting/commenting","WhatsApp / Email outreach","Referral-based work","Digital marketing basics","Sales / BDE work"].includes(exp.trim())) score += 5;
});

// Role understanding
if(row["This role is NOT a full-time job and has NO fixed salary. Do you understand this?"] == "Yes, I understand") score += 20;

switch(row["How much time can you realistically give per day?"]) {
case "30 minutes": score +=5; break;
case "1 hour": score +=10; break;
case "2+ hours": score +=15; break;
}

switch(row["What device will you use for this role?"]) {
case "Mobile only": score +=5; break;
case "Laptop only": score +=10; break;
case "Both mobile & laptop": score +=15; break;
}

if(row["This role offers performance-based pocket-money income (approx. USD 50–150/month). Are you comfortable with this?"] == "Yes") score +=20;
if(row["Why are you interested in the Growth Partner role at NIVY?"] && row["Why are you interested in the Growth Partner role at NIVY?"].length>10) score +=10;

// Skills & Network
const platforms = row["Which platforms are you active on?"] ? row["Which platforms are you active on?"].split(",") : [];
platforms.forEach(p => { if(p.trim()!="None") score +=5; });

switch(row["Do you have access to business owners, professionals, or startup communities?"]) {
case "Yes": score +=10; break;
case "Not sure": score +=5; break;
}

// Final confirmation
if(row["I confirm that:"] && row["I confirm that:"].includes("This is a part-time, contribution-based role")) score +=20;

return score;
}

// Send email function
function sendEmail(toEmail, subject, body) {
MailApp.sendEmail({
to: toEmail,
subject: subject,
htmlBody: body
});
}

// Trigger function on form submit
function onFormSubmit(e) {
const row = e.namedValues;
const email = row["Email Address"][0];
const name = row["Full Name"][0];

// Flatten row
const formattedRow = {};
for(let key in row) formattedRow[key] = row[key][0];

const score = calculateScore(formattedRow);

// Confirmation email
const confirmationBody =   `<p>Hello ${name},</p>   <p>Thank you for applying for the <b>Growth Partner (Part-Time | Remote)</b> role at ${COMPANY_NAME}.</p>   <p>✅ We have received your application.</p>   <p><b>Important:</b><br>- Part-time role<br>- Performance-based income (USD 50–150/month)</p>   <p>Our team will review your application.</p>   <p>🌐 <a href="${COMPANY_WEBSITE}">${COMPANY_NAME}</a><br>📧 ${HR_EMAIL}</p>`  ;
sendEmail(email, `Application Received – ${COMPANY_NAME} Growth Partner`, confirmationBody);

// Selection/Rejection email
if(score >= MIN_SCORE){
const selectionBody =     `<p>Hello ${name} 👋</p>     <p>Congratulations! You have been <b>selected</b> for the ${COMPANY_NAME} Growth Partner role.</p>     <p>Next steps: Join group, review onboarding, start contributing.</p>     <p>💰 Earnings: USD 50–150/month, per client.<br>💻 Mobile/Laptop + Internet required.</p>     <p>📩 Contact: ${HR_EMAIL}</p>     <p>Welcome aboard! 🚀</p>`    ;
sendEmail(email, `Congratulations! Selected – ${COMPANY_NAME} Growth Partner`, selectionBody);
} else {
const rejectionBody =     `<p>Hello ${name},</p>     <p>Thank you for applying. After review, you were <b>not shortlisted</b>.</p>     <p>You may reapply in future opportunities.</p>     <p>🌐 <a href="${COMPANY_WEBSITE}">${COMPANY_NAME}</a><br>📧 ${HR_EMAIL}</p>`    ;
sendEmail(email, `Application Update – ${COMPANY_NAME} Growth Partner`, rejectionBody);
}
}