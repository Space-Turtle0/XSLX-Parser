from core.csv_parser import combine_files_to_excel, get_files
from core.email_endpoint import get_gmail_service, create_message_with_attachment, send_message

_to_email = "example@example.com"
_EMAIL_SERVICE = True

if __name__ == "__main__":
    input_files = get_files()
    output_file = 'combined_output.xlsx'

    combine_files_to_excel(input_files, output_file)

    if _EMAIL_SERVICE:
        # Send the email with the attachment
        service = get_gmail_service()
        email_message = create_message_with_attachment(
            to=_to_email,
            subject='Combined Excel File',
            message_text='Please find the attached combined Excel file.',
            file_path=output_file
        )
        send_message(service, 'me', email_message)
