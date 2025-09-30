<script>
  import { onMount } from "svelte";

  let password = "";
  let error = "";
  let loggedIn = false;
  let role = "";

  async function submitPassword() {
    error = "";
    const formData = new FormData();
    formData.append("password", password);

    const res = await fetch("http://localhost:8000/api/login", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    if (data.success) {
      loggedIn = true;
    } else {
      error = data.error;
    }
  }

  function selectRole(r) {
    role = r;
  }
</script>

{#if !loggedIn}
  <h1>Enter Password</h1>
  <input
    type="password"
    bind:value={password}
    placeholder="Password"
    on:keydown={(e) => e.key === 'Enter' && submitPassword()}
  />
  <button on:click={submitPassword}>Login</button>
  {#if error}<p style="color:red">{error}</p>{/if}
{:else if !role}
  <h1>Select Role</h1>
  <button on:click={() => selectRole("trainer")}>Trainer</button>
  <button on:click={() => selectRole("athlete")}>Athlete</button>
{:else}
  <h1>Welcome, {role}!</h1>
{/if}