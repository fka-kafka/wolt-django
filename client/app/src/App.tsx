import Form from "./components/Form.tsx";
import { FormProvider } from "./contexts/FormContext.tsx";
import 'vite/modulepreload-polyfill'

function App() {
  return (
    <FormProvider>
      <Form />
    </FormProvider>
  );
}

export default App;
