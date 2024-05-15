import tabulate as tab

from scraper import get_replacement


def table_format(lst):
    return tab.tabulate(lst, tablefmt="plain")


def save_html_to_file(html_content):
    with open("Заміни.html", "w", encoding="utf-8") as file:
        file.write(html_content)


def get_replacement_html(replacement):
    html = """
  <!DOCTYPE html>
  <html>
  <head>   
      <meta charset="UTF-8">
      <title>Заміни</title>
      <style>
          table {
              border-collapse: collapse;
              width: 100%;
          }

          th, td {
              border: 1px solid #ddd;
              padding: 8px;
          }

          th {
              text-align: left;
          }
      </style>
  </head>
  <body>
  <h1>{replacement[0]}</h1>
  <table>
      <tr>
          <th>Група</th>
          <th>№</th>
          <th>Кого замінили</th>
          <th>Предмет</th>
          <th>Викладач</th>
          <th>Ауд.</th>
      </tr>
  """

    for row in range(2, len(replacement)):
        html += f"""
          <tr>
              <td>{replacement[row][0]}</td>
              <td>{replacement[row][1]}</td>
              <td>{replacement[row][2]}</td>
              <td>{replacement[row][3]}</td>
              <td>{replacement[row][4]}</td>
              <td>{replacement[row][5]}</td>
          </tr>
      """

    html += """
  </table>
  </body>
  </html>
  """

    return html
