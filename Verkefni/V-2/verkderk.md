<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verkefni 2. sýnidæmi</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body class="container">
    <h1>Verkefni 2</h1>
    <h3>Dagskrá í töflu sem aðlagast öllum skjástærðum</h3>
    <div class="schedule">
      <table>
        <caption>Schedule of something</caption>
        <thead>
            <tr> 
                <th scope="col">WHO</th>
                <th scope="col">WHERE</th>
                <th scope="col">WHEN</th>
                <th scope="col">CHECK IN</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td scope="row">Obcaecati deleniti</td>
                <td>Lorem ipsum dolor, adipisicing elit</td>
                <td>10:30 - 12:00</td>
                <td><button>Register</button></td>
            </tr>
            <tr>
                <td scope="row">Sit amet consectetur</td>
                <td>Dolor saepe odio</td>
                <td>13:30 - 17:00</td>
                <td><button>Register</button></td>
            </tr>
            <tr>
                <td scope="row">Fuga corrupti commodi optio</td>
                <td>Non eius odit, animi alias adipisci sed hic nisi.</td>
                <td>22:30 - 00:00</td>
                <td><button>Register</button></td>
            </tr>
            <tr>
              <td scope="row">Obcaecati deleniti</td>
              <td>Lorem ipsum dolor, adipisicing elit</td>
              <td>10:30 - 12:00</td>
              <td><button>Register</button></td>
          </tr>
          <tr>
              <td scope="row">Sit amet consectetur</td>
              <td>Dolor saepe odio</td>
              <td>13:30 - 17:00</td>
              <td><button>Register</button></td>
          </tr>
          <tr>
              <td scope="row">Fuga corrupti commodi optio</td>
              <td>Non eius odit, animi alias adipisci sed hic nisi.</td>
              <td>22:30 - 00:00</td>
              <td><button>Register</button></td>
          </tr>
        </tbody>
      </table>
    </div>




    <table>
        <caption>Titill töflu</caption>
        <thead>
            <tr>
                <th scope="col"> </th>
                <th scope="col">A</th>
                <th scope="col">B</th>
                <th scope="col">C</th>
                <th scope="col">D</th>
            </tr>
            <!-- The scope attribute specifies whether a header cell is a header for a column, row, or group of columns or rows.
            Note: The scope attribute has no visual effect in ordinary web browsers, but can be used by screen readers. -->
        </thead>
        <tbody>
            <tr>
                <td scope="row" data-label="AÖ">E</td>
                <td data-label="A">Atli</td>
                <td data-label="B">Bára</td>
                <td data-label="C">Cesar</td>
                <td data-label="D">Dóra</td>
            </tr>
            <tr>
                <td scope="row" data-label="AÖ">F</td>
                <td data-label="A">Andrés</td>
                <td data-label="B">Baldur</td>
                <td data-label="C">Cleopatra</td>
                <td data-label="D">Daníel</td>
            </tr>
            <tr>
                <td scope="row" data-label="AÖ">G</td>
                <td data-label="A">Alfreð</td>
                <td data-label="B">Björn</td>
                <td data-label="C">Calicula</td>
                <td data-label="D">Diðrik</td>
            </tr>
        </tbody>
    </table>	







</body>
</html>