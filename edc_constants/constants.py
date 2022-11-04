import re

ABNORMAL = "ABNORMAL"
ABSENT = "absent"
ADDITIONAL = True
AFTERNOON = "afternoon"
ALIVE = "alive"
ANONYMOUS = "anonymous"
ANYTIME = "anytime"
AWAITING_RESULTS = "awaiting_results"
BLACK = "black"
BY_BIRTH = "BY_BIRTH"
CANCELLED = "cancelled"
CHOL = "chol"
CLINIC = "clinic"
CLINICAL_ENDPOINT = "clinical_endpoint"
CLINICAL_WITHDRAWAL = "clinical_withdrawal"
CLOSED = "closed"
COLLATERAL_HISTORY = "collateral_history"
COMPLETE = "COMPLETE"
CONSENTED = "consented"
CONTINUOUS = "continuous"
CONTROL = "control"
CREATE = "CREATE"
DEAD = "dead"
DECEASED = "dead"
DECLINED = "Declined"
DECREASED = "decreased"
DEFAULTER = "defaulter"
DELETE = "DELETE"
DELIVERY = "delivery"
DIABETES = "diabetes"
DM = "dm"
DONE = "done"
DONT_KNOW = "dont_know"
DWTA = "DWTA"  # don't want to answer'
ERROR = "ERROR"
EVENING = "evening"
FAILED_ELIGIBILITY = "failed eligibility"
FALSE = "false"
FASTING = "fasting"
FEEDBACK = "feedback"
FEMALE = "F"
FORMER_SMOKER = "former_smoker"
FREE_OF_CHARGE = "free"
HEADACHE = "headache"
HELD = "held"
HIDE_FORM = "NOT_REQUIRED"
HIGH = "high"
HIGH_PRIORITY = "high"
HIV = "HIV"
HOSPITAL = "hospital"
HOSPITALIZED = "hospitalized"
HOSPITAL_NOTES = "hospital_notes"
HOSPITAL_OR_CLINIC = "hospital_or_clinic"
HTN = "htn"
HYPERTENSION = "hypertension"
IGNORE = "ignore"
INCOMPLETE = "INCOMPLETE"
IND = "IND"
INITIAL = "initial"
INSERT = "INSERT"
INTERVENTION = "intervention"
IN_PERSON = "in_person"
LIVE = "live"
LOW = "low"
LOW_PRIORITY = "low"
MALE = "M"
MALIGNANCY = "malignancy"
MEDIUM_PRIORITY = "medium"
MICROSCOPY = "microscopy"
MOBILE_NUMBER = "mobile_no"
MODIFIED = "modified"
MORNING = "morning"
NAIVE = "NAIVE"
NCD = "NCD"
NEG = "NEG"
NEVER = "NEVER"
NEW = "New"
NEW_FIELD = "new_field"
NEXT_OF_KIN = "next_of_kin"
NO = "No"
NON_BLACK = "non_black"
NONE = "none"
NONSMOKER = "nonsmoker"
NON_FASTING = "non_fasting"
NORMAL = "NORMAL"
NOT_ADDITIONAL = False
NOT_ANSWERED = "not_answered"
NOT_APPLICABLE = "N/A"
NOT_DONE = "not_done"
NOT_ESTIMATED = "not_estimated"
NOT_EVALUATED = "not_evaluated"
NOT_EXAMINED = "not_examined"
NOT_RECORDED = "not_recorded"
NOT_REQUIRED = "not_required"
NOT_SURE = "not_sure"
NOT_TESTED = "not_tested"
NO_EXAM = "NO_EXAM"
NO_UNCONFIRMED = "no_unconfirmed"
OBSERVATION = "observation"
OFF_STUDY = "off study"
OFF_STUDY_VISIT = "off study"
OMANG = "OMANG"
ON_ART = "on_art"
ON_STUDY = "on study"
OPEN = "open"
OPTIONAL = True
OTHER = "OTHER"
OTHER_PLEASE_SPECIFY_TEXT = "Other, please specify below ..."
OUTPATIENT_CARDS = "outpatient_cards"
PARTIAL = "PARTIAL"
PARTICIPANT = "participant"
PATIENT = "patient"
PATIENT_REPRESENTATIVE = "patient_representative"
PENDING = "PENDING"
PER_PROTOCOL = "per_protocol"
POS = "POS"
PREGNANCY = "pregnancy"
PRESENT = "present"
PRESENT_WITH_REINFORCEMENT = "present_with_reinforcement"
PRIMARY = "primary"
PRINT = "PRINT"
PURPOSIVELY_SELECTED = "purposively_selected"
QUERY = "QUERY"
QUESTION_RETIRED = "QUESTION_RETIRED"
RANDOM_SAMPLING = "random_sampling"
RAPID_TEST = "rapid_test"
REDUCED = "reduced"
REFILL = "refill"
REFUSED = "REFUSED"
RESOLVED = "resolved"
RESTARTED = "restarted"
ROUTINE_VISIT = "routine_visit"
SCREENED = "SCREENED"
SECONDARY = "secondary"
SEQUENTIAL = "sequential"
SEROCONVERSION = "seroconversion"
SHOW_FORM = "NEW"
SMOKER = "smoker"
STEROIDS = "steroids"
STOPPED = "stopped"
STUDY_DEFINED_TIMEPOINT = "study_defined_timepoint"
SUBJECT = "subject"
SYSTEMATIC = "systematic"
TBD = "tbd"  # to be determined
TELEPHONE = "telephone"
TERTIARY = "tertiary"
TEST = "test"
TOXICITY = "toxicity"
TRUE = "true"
TUBERCULOSIS = "TB"
UNK = "UNK"
UNKNOWN = "unknown"
UNWELL_VISIT = "unwell_visit"
UPDATE = "UPDATE"
UUID_PATTERN = re.compile(
    "[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}"
)
VIEW = "VIEW"
VISUAL_LOSS = "visual_loss"
WARN = "warn"
WEEKDAYS = "weekdays"
WEEKENDS = "weekends"
YES = "Yes"


FUTURE_DATE = "future_date"
LAST_WEEK = "last_week"
NEXT_WEEK = "next_week"
NOT_NULL = "not_null"
IS_NULL = "is_null"
PAST_DATE = "past_date"
THIS_WEEK = "this_week"
TODAY = "today"
TOMORROW = "tomorrow"
YESTERDAY = "yesterday"
