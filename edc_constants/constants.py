import re

UUID_PATTERN = re.compile(
    "[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}"
)

ABNORMAL = "ABNORMAL"
ABSENT = "absent"
ADDITIONAL = True
AFTERNOON = "afternoon"
ALIVE = "alive"
ALWAYS = "always"
ANONYMOUS = "anonymous"
ANYTIME = "anytime"
AWAITING_RESULTS = "awaiting_results"
BLACK = "black"
BOTH = "both"
BY_BIRTH = "BY_BIRTH"
CANCELLED = "cancelled"
CHOL = "chol"
CLINIC = "clinic"
CLINICAL_ENDPOINT = "clinical_endpoint"
CLINICAL_WITHDRAWAL = "clinical_withdrawal"
CLINICIAN = "clinician"
CLOSED = "closed"
COLLATERAL_HISTORY = "collateral_history"
COMPLETE = "COMPLETE"
COMMUNITY = "community"
CONFIRMED = "confirmed"
CONSENTED = "consented"
CONTINUOUS = "continuous"
CONTROL = "control"
CREATE = "CREATE"
DEAD = "dead"
DECEASED = "dead"
DECLINED = "Declined"
DECREASED = "decreased"
DEFAULTED = "defaulted"
DEFAULTER = "defaulter"
DELETE = "DELETE"
DELIVERY = "delivery"
DIABETES = "diabetes"
DIVORCED = "divorced"
DM = "dm"
DONE = "done"
DONT_KNOW = "dont_know"
DWTA = "DWTA"  # don't want to answer
ERROR = "ERROR"
ESTIMATED = "estimated"
EVENING = "evening"
FAILED_ELIGIBILITY = "failed eligibility"
FALSE = "false"
FASTING = "fasting"
FEEDBACK = "feedback"
FEMALE = "F"
FORMER_SMOKER = "former_smoker"
FREE_OF_CHARGE = "free"
FUTURE_DATE = "future_date"
HEADACHE = "headache"
HELD = "held"
HIDE_FORM = "NOT_REQUIRED"
HIGH = "high"
HIGH_PRIORITY = "high"
HIV = "HIV"
HOME = "home"
HOSPITAL = "hospital"
HOSPITALIZED = "hospitalized"
HOSPITAL_NOTES = "hospital_notes"
HOSPITAL_OR_CLINIC = "hospital_or_clinic"
HTN = "htn"
HYPERTENSION = "hypertension"
IGNORE = "ignore"
IN_PROGRESS = "in_progress"
INCOMPLETE = "INCOMPLETE"
IND = "IND"
INITIAL = "initial"
INPATIENT = "inpatient"
INSERT = "INSERT"
INSURANCE = "insurance"
INTEGRATED = "integrated"
INTEGRATED_CLINIC = "integrated_clinic"
INTERVENTION = "intervention"
INVESTIGATOR = "investigator"
INVESTIGATOR_DECISION = "investigator_decision"
IN_PERSON = "in_person"
IS_NULL = "is_null"
LAST_MONTH = "last_month"
LAST_WEEK = "last_week"
LIVE = "live"
LOW = "low"
LOW_PRIORITY = "low"
MALE = "M"
MALIGNANCY = "malignancy"
MARRIED = "married"
MEDIUM_PRIORITY = "medium"
MEASURED = "measured"
MICROSCOPY = "microscopy"
MOBILE_NUMBER = "mobile_no"
MODIFIED = "modified"
MONTHLY = "monthly"
MORNING = "morning"
MULTI_MORBIDITY = "multi"
NAIVE = "NAIVE"
NCD = "NCD"
NEG = "NEG"
NEVER = "NEVER"
NEW = "New"
NEW_FIELD = "new_field"
NEXT_OF_KIN = "next_of_kin"
NEXT_WEEK = "next_week"
NO = "No"
NONE = "none"
NONSMOKER = "nonsmoker"
NON_BLACK = "non_black"
NON_FASTING = "non_fasting"
NORMAL = "NORMAL"
NOT_ADDITIONAL = False
NOT_ANSWERED = "not_answered"
NOT_APPLICABLE = "N/A"
NOT_AVAILABLE = "not_available"
NOT_DONE = "not_done"
NOT_ESTIMATED = "not_estimated"
NOT_EVALUATED = "not_evaluated"
NOT_EXAMINED = "not_examined"
NOT_NULL = "not_null"
NOT_RECORDED = "not_recorded"
NOT_REQUIRED = "not_required"
NOT_SURE = "not_sure"
NOT_TESTED = "not_tested"
NO_EXAM = "NO_EXAM"
NO_UNCONFIRMED = "no_unconfirmed"
OBSERVATION = "observation"
OK = "OK"
OFF_STUDY = "off study"
OFF_STUDY_VISIT = "off study"
OMANG = "OMANG"
ON_ART = "on_art"
ON_STUDY = "on study"
ONGOING = "ongoing"
OPEN = "open"
OPTION_RETIRED = "OPTION_RETIRED"
OPTIONAL = True
OTHER = "OTHER"
OTHER_PLEASE_SPECIFY_TEXT = "Other, please specify below ..."
OUTPATIENT_CARDS = "outpatient_cards"
OUTPATIENT = "outpatient"
OWN_CASH = "own_cash"
PARTIAL = "PARTIAL"
PARTICIPANT = "participant"
PAST_DATE = "past_date"
PATIENT = "patient"
PATIENT_CLUB = "club"
PATIENT_REPRESENTATIVE = "patient_representative"
PENDING = "PENDING"
PER_PROTOCOL = "per_protocol"
POS = "POS"
PREGNANCY = "pregnancy"
PRESENT = "present"
PRESENT_WITH_REINFORCEMENT = "present_with_reinforcement"
PRIMARY = "primary"
PRINT = "PRINT"
PRIVATE = "private"
PURPOSIVELY_SELECTED = "purposively_selected"
QUERY = "QUERY"
QUESTION_RETIRED = "QUESTION_RETIRED"
RANDOM_SAMPLING = "random_sampling"
RAPID_TEST = "rapid_test"
RARELY = "rarely"
RECEIVED = "received"
REDUCED = "reduced"
REFILL = "refill"
REFUSED = "REFUSED"
RELATIVE = "relative"
RESOLVED = "resolved"
RESTARTED = "restarted"
ROUTINE_VISIT = "routine_visit"
SAE = "sae"
SCREENED = "SCREENED"
SECONDARY = "secondary"
SEQUENTIAL = "sequential"
SEROCONVERSION = "seroconversion"
SHOW_FORM = "NEW"
SINGLE = "single"
SMOKER = "smoker"
SOMETIMES = "sometimes"
STEROIDS = "steroids"
STOPPED = "stopped"
STUDY_DEFINED_TIMEPOINT = "study_defined_timepoint"
SUBJECT = "subject"
SYSTEMATIC = "systematic"
TBD = "tbd"  # to be determined
TELEPHONE = "telephone"
TERTIARY = "tertiary"
TEST = "test"
THIS_MONTH = "this_month"
THIS_WEEK = "this_week"
TIMEPOINT = "timepoint"
TODAY = "today"
TOMORROW = "tomorrow"
TOXICITY = "toxicity"
TRUE = "true"
TUBERCULOSIS = "TB"
UNK = "UNK"
UNKNOWN = "unknown"
UNWELL_VISIT = "unwell_visit"
UPDATE = "UPDATE"
VERY_OFTEN = "very_often"
VIEW = "VIEW"
VISUAL_LOSS = "visual_loss"
WARN = "warn"
WEEKDAYS = "weekdays"
WEEKENDS = "weekends"
WEEKLY = "weekly"
WIDOWED = "widowed"
YEARLY = "yearly"
YES = "Yes"
YESTERDAY = "yesterday"

# operators
EQ = "="
GT = ">"
GTE = ">="
LT = "<"
LTE = "<="

# days of the week
MONDAY = "monday"
TUESDAY = "tuesday"
WEDNESDAY = "wednesday"
THURSDAY = "thursday"
FRIDAY = "friday"
SATURDAY = "saturday"
SUNDAY = "sunday"
