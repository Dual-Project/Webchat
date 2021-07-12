<template>
  <section>
      <div class="name">
          <!--Usar o double mustache no username e puxar no banco-->
          <h1>Username</h1>
      </div>

      <div class="description">
          <h5>Description</h5>
      </div>
  </section>
</template>

<script>
export default {
    name: 'User',
    props: {
        username: String
    }
}
</script>

<style scoped>
:root{
    --light: #fff;
    --dark: #242424;
    --semi-light: #949494;
    --semi-dark: #454545;
    --primary: #f93;

    --radius: 15px;
}

*{
    margin: 0;
    padding: 0;
}

section{
    padding-left: 1em;
}

section div.name{
    font-size: 1rem;
    color: var(--dark)
}

h5{
    color: #949494;

}
</style>